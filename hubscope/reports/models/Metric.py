
from django.db import models
from django.db.models import Q
from .utils import DayRange
from decimal import ROUND_UP, Decimal
from django.utils.timezone import localdate
from functools import reduce
from termcolor import cprint
from django.core.exceptions import ValidationError
class Metric(models.Model):
    '''
        Indicador Reportado   
    '''
    TIPOS = [
        ('A','Acumulativa'),
        ('E','Estado'),
        ('C','Constante'),
        ('COMP','Computada')
    ]
    name = models.CharField(unique=True, max_length=100)
    tipo = models.CharField(choices=TIPOS, blank=True, max_length=100, default='A')
    unidad = models.CharField(max_length=50, blank=True)
    desc = models.TextField()
    dependencies = models.ManyToManyField('self')

    class Meta:
        verbose_name = "Metric"
        verbose_name_plural = "Metrics"
        
    def __init__(self, *args, **kwargs):
        self.constant_value = kwargs.pop('value', None)
        # if kwargs['tipo'] == 'C' and self.constant_value is None:
        #     raise Exception('Debe Asignarse un valor por defecto a la constante')
        super(Metric, self).__init__(*args, **kwargs)


    def __str__(self):
        return f'{self.name} {self.tipo}'
    
    def save(self, *args, **kwargs):
        if self.tipo == 'C' and self.constant_value is None:
            raise ValidationError('Toda Constnte requiere un valor')
        super(Metric, self).save(*args, **kwargs)
        if self.tipo == 'C':
            if self.responses.count()==0:
                self.responses.create_constant(self, self.constant_value)
        return self

    @property
    def value_of_constant(self):
        if self.tipo == 'C':
            return self.responses.filter(end=None).last().value
        return None

        
    def reports(self, **kwargs):
        ''' Optiene los reportes de una metrica especifica'''
        query = {}
        end = kwargs.get('end', localdate())
        begin = kwargs.get('begin')


        # import pdb; pdb.set_trace()
        if self.tipo in ['C','E']:
            self.responses.update_state(self)
            full_cover = self.responses.filter(begin__lte=begin, end__gte=end)
            if full_cover:
                return full_cover
            full_cover_active =  self.responses.filter(begin__lte=begin, end=None)
            if full_cover_active:
                return full_cover_active

            partial_cover_active =  self.responses.filter(begin__lte=end, end=None)
            if partial_cover_active:
                complement = self.responses.filter(end__gte=begin)
                responses = partial_cover_active | complement
                return responses.order_by('begin')
            
            return self.responses \
                .filter(~ Q(end__lte = begin)) \
                .filter(~ Q(begin__gte = end)) \
                .order_by('begin')


            # return self.responses \
            #     .filter(begin__lte=end, company=kwargs['company']) \
            #     .filter(Q(end=None) | Q(end=False))
            #     .order_by('begin')

        for k,v in kwargs.items():
            if k == 'begin':
                query['end__gte'] = v
            elif k == 'end':
                query['begin__lte'] = v
            else:
                query[k] = v

        return self.responses \
            .filter(~ Q(value = None)) \
            .filter(**query).order_by('begin')
    
    def _get_filtered_reports(self, dayrange, company=None):
        query = {
            'begin':dayrange.begin,
            'end':dayrange.end,
        }
        
        if company:
            query['company'] = company
        return  self.reports(**query)
            
    def __get_value_from(self, day, reports):
        for report in reports:
            if report.dayrange.includes(day):
                return report.daily_value
        return 0

    def agregated_results(self, dayrange, company=None):
        reports = self._get_filtered_reports(dayrange, company)
        agregator = 0
        for day in dayrange.days:
            agregator = agregator + self.__get_value_from(day, reports)
        return Decimal(agregator).quantize(Decimal('.01'),rounding=ROUND_UP)

    def results_by_day(self, dayrange, company=None):
        reports = self._get_filtered_reports(dayrange, company)
        cprint( len(reports), 'white', 'on_blue')
        results_by_day = []
        for day in dayrange.days:
            results_by_day.append({
                'date':day,
                'value':self.__get_value_from(day, reports)
            })
        return results_by_day
            
    def __covered_days__(self, reportsqs):
        days_by_report = [r.reported_days() for r in reportsqs]
        reported_days = reduce(lambda x,y:x+y, days_by_report, [])
        return reported_days

    def __missing_days__(self, dayrange, reportsqs):
        covered = self.__covered_days__(reportsqs)
        return [d for d in dayrange.days if d not in covered]
    
    def __overlaped_days__(self, reportsqs):
        covered = self.__covered_days__(reportsqs)
        return {d for d in covered if covered.count(d) > 1 }


    def days_reported(self, dayrange, company=None):
        reports = self._get_filtered_reports(dayrange, company)
        days_reported = {
            'to_cover':dayrange.days,
            'covered':self.__covered_days__(reports),
            'missing': self.__missing_days__(dayrange, reports) ,
            'overlaped':self.__overlaped_days__(reports) 
        }
        return days_reported


