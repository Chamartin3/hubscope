import calendar 
from django.db import models
from datetime import  datetime, timedelta, date
from django.utils.timezone import localdate
from hubscope.accounts.models import User
from django.core.exceptions import ValidationError
from django.core.validators import int_list_validator
from functools import reduce
from django.db.models import Q
from .utils import DayRange


from .Metric import Metric
from .Company import Company



class ReportsManager(models.Manager):
    def by_company(self,company):
        self.filter(company=company)

    def by(self, **kwargs):
        ''' Optiene los reportes filtrados por 
        tiempo begin, end
        compañia
        o metrica
        '''
        

        for k,v in kwargs.items():
            if k == 'begin':
                query['begin__gte'] = v
            elif k == 'end':
                query['end__lte'] = v
            else:
                query[k] = v

        return self.filter(**query)

    def by_status(self, param):

        if param == 'cerrada':
            return self.filter( editable=False )
        
        qs = self.filter(editable=True).filter(~Q(end=None))
        if param == 'entregada':
            return qs.filter(~Q(value=None))
        
        qs = qs.filter(value=None)
        if param == 'esperando':
            return qs.filter(end__gte=localdate() )
            
        qs = qs.filter(end__lt=localdate())
        if param == 'abierta':
            return qs.filter(deadline__gt=localdate() )
        
        if param == 'atrasada':
            return qs.filter(deadline__lt=localdate() )

        
        print( f'{param} is not a recogniced status for Reports' )  
        import pdb; pdb.set_trace()
        raise 


    def create_constant(self, metric, value):
        # import pdb; pdb.set_trace()
        if metric.tipo != 'C':
            raise ValidationError("La metrica no es una constante pero se esta curdando un reporte como tal")
        report = {
            'constant': True,
            'editable': False,
            'value': value,
            'metric': metric,
            'company': None,
            'begin': date(year=2000, month=1, day=1)
        }
        constant_value = self.model(**report)
        
        return constant_value.save()
    
    def get_next(self, new_begin):
        return self.filter(begin__gt=new_begin).order_by('begin')

    def get_last(self, new_begin):
        prev = self.filter(begin__lt=new_begin, end=None)
        if prev.count() >= 1 :
            return prev
        
        prev = self.filter(begin__lt=new_begin).order_by('-end')
        if prev.count() == 0:
            return None
        
        return prev[0]
    
    def update_state(self,metric):
        if metric.tipo not in ['C', 'E']:
            return
        active_reports=self.filter(end=None, metric=metric).order_by('-begin')
        if active_reports.count() > 1:
            for idx, report in enumerate(active_reports):
                if idx == 0:
                    continue
                prev_date = active_reports[idx-1].begin
                new_end = prev_date - timedelta(days=1)
                self.filter(pk=report.pk) \
                    .update(end=new_end, editable=False)

class Report(models.Model):
    """Es el Registro de información cruda """
    metric = models.ForeignKey(Metric,
        on_delete=models.CASCADE, 
        related_name='responses'
    )    
    company = models.ForeignKey(Company,
        on_delete=models.CASCADE, 
        null=True,
        blank=True,
        related_name='reports'
    )
    begin = models.DateField()
    end = models.DateField(blank=True, null=True)
    constant = models.BooleanField(default=False, blank=True)

    # Traking Data 
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    registered_by = models.ForeignKey(User,
        blank=True, null=True,
        on_delete=models.CASCADE, 
        related_name='reg_creados'
    )
    updated_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User,
        blank=True, null=True,
        on_delete=models.CASCADE, 
        related_name='reg_modificados'
    )

    editable = models.BooleanField(default=True)

    # Valor testual io numerico
    value = models.FloatField(blank=True, null=True)
    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    objects = ReportsManager()

    
    def close(self):
        if self.value:
            self.editable = False
            return self.save()
        return None


    def clean(self):
        if self.begin is None:
            raise ValidationError("un inicio es requerido")
        if self.metric.tipo in ['C', 'E']:
            return

        if self.end is None:
            raise ValidationError("un final es requerido")

        if self.begin > self.end:
            import pdb; pdb.set_trace()
            raise ValidationError("La fecha fecha de inicio no puede ser posterior a la fecha de finalización")


    def create(self, *args, **kwargs):
        try:
            return super().create(*args, **kwargs)
        except:
            import pdb; pdb.set_trace()
    def save(self, *args, **kwargs):
        self.full_clean()
        fist_time = self.created_at is None
        if self.value is not None and fist_time:
            self.created_at = localdate()
                
        if self.metric.tipo in ['C', 'E']:
            kwargs.pop('end', None)
            self.end = None 
            # nextr = self.objects.get_next(self.begin)
            # if nextr:
            #     self.end = nextr[0].begin  - timedelta(days=1)

        super().save(*args, **kwargs)

        # if self.metric.tipo in ['C', 'E']:
        #     last = self.objects.get_last(self.begin)
        #     if nextr:
        #         end = self.begin - timedelta(days=1)
        #         nextr.update(end=end)
        return self




    def fill(self, value, registered_by):
        if self.value is not None:
            self.modified_by = registered_by
        else:
            self.registered_by = registered_by
        self.value = value
        
        # import pdb; pdb.set_trace()
        saved = self.save()
        if self.asignment.exists():
            self.asignment.get().save() 
        return saved



    @property
    def days(self):
        return self.dayrange.size

    @property
    def daily_value(self):
        if self.metric.tipo == 'A':
            return self.value / self.days
        else:
            return self.value
    
    @property
    def dayrange(self):
        return DayRange(self.begin, self.end)

    def reported_days(self):
        return self.dayrange.days

    @property
    def delay(self):
        if self.deadline is None:
            return 0
        delivered = self.created_at
        if delivered is not None:
            # import pdb; pdb.set_trace()
            return (delivered.date() - self.deadline).days -1
        return (localdate() - self.deadline).days -1
    

    
    @property
    def delayed(self):
        return self.delay > 0

    @property
    def status(self):
        if self.metric.tipo in ['C', 'E']:
            if self.end is None:
                return 'activa'
            else:
                return 'cerrada'

        if not self.editable:
            return 'cerrada'

        if self.value is not None:
            return 'entregada'

        waiting = (self.end -localdate()).days
        if(waiting > -1):
            return 'esperando'
        
        dl = self.deadline if self.deadline is not None else localdate() 
        is_open = (dl - localdate()).days
        if(is_open>-1):
            return 'abierta'

        return 'atrasada'
    @property
    def creator(self):
        if self.registered_by is None:
            return 'sistema'
        return self.registered_by.fullname    
    
    @property
    def editor(self):
        if self.modified_by is None:
            return 'sistema'
        return self.modified_by.fullname
        

    def __str__(self):
        """Unicode representation of Response."""
        return f'{self.metric}({self.created_at}): {self.value}'

