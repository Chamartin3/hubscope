import calendar 
from django.db import models
from datetime import  datetime, timedelta
from django.utils.timezone import localdate
from hubscope.accounts.models import User
from django.core.exceptions import ValidationError
from django.core.validators import int_list_validator
from functools import reduce
from django.db.models import Q


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
        
        qs = self.filter(editable=True)
        if param == 'entregada':
            return qs.filter(~Q(num_value=None))
        
        qs = qs.filter(num_value=None)
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

class Report(models.Model):
    """Es el Registro de información cruda """
    metric = models.ForeignKey(Metric,
        on_delete=models.CASCADE, 
        related_name='responses'
    )    
    company = models.ForeignKey(Company,
        on_delete=models.CASCADE, 
        related_name='reports'
    )
    begin = models.DateField()
    end = models.DateField()

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
    num_value = models.FloatField(blank=True, null=True)
    text_value = models.CharField(blank=True, null=True, max_length=50)
    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    objects = ReportsManager()

    
    def clean(self):
        if self.begin > self.end:
            raise ValidationError("La fecha fecha de inicio no puede ser posterior a la fecha de finalización")

    def save(self, *args, **kwargs):
        self.full_clean()
        fist_time = self.created_at is None
        if self.value is not None and fist_time:
            self.created_at = localdate()
        return super().save(*args, **kwargs)

    @property
    def value(self):
        m = self.metric
        if m.tipo == 'C':
            return self.num_value
        return self.text_value

    @property
    def days(self):
        return (self.end-self.begin).days +1

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
        if not self.editable:
            return 'cerrada'

        if self.value is not None:
            return 'entregada'

        waiting = (self.end -localdate()).days
        if(waiting > -1):
            return 'esperando'

        is_open = (self.deadline - localdate()).days
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

