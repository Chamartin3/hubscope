from .Metric import Metric
from .Company import Company, Position
from .Reports import Report
from .ProcesingCallbacks import procesing as PCallbacks
from .Informe import Informe


from django.db import models
from functools import reduce

from .utils import DayRange


import calendar 
from django.db.models import Q
from datetime import  datetime, timedelta, date
from django.utils.timezone import localdate
from hubscope.accounts.models import User
from decimal import ROUND_UP, Decimal

from django.core.exceptions import ValidationError
from django.core.validators import int_list_validator
# from functools import reduce
from termcolor import cprint




class Components(models.Model):
    metrica = models.ForeignKey('Metric',  
        null=True,  
        on_delete=models.SET_NULL)
    indicator = models.ForeignKey('Indicator',
        related_name='components', 
        null=True,  on_delete=models.SET_NULL)
    role = models.CharField(max_length=50) 

    def __str__(self):
        return f'{self.role} {self.metrica}'


class Indicator(models.Model):
    '''
        Define las unidades de medida compuestas por uno 
        o mas metricas de una compañia, asi como una meta  para un periodo especifico
    '''
    ITYPES =(
        ('S','Simple' ),
        ('E','Estado'),
        ('A','Acumulado'), #Por eliminar
        ('C','Cociente'),
        ('P', 'Porcentaje'),
        ('SA','Producto') # Por Definir
    ) 
    name = models.CharField(blank=True, max_length=100)
    unidad = models.CharField(max_length=50)
    desc = models.TextField()
    tipo = models.CharField(choices=ITYPES, max_length=2, default="A")
    active = models.BooleanField(default=True)
    metrics = models.ManyToManyField(Metric, 
        through='Components',
        related_name='indicators') 
    company = models.ForeignKey(Company,
        null=True, blank=True,
        related_name='indicators', 
        on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'

    def __str__(self):
        return f'{self.name}:{self.tipo}'
    
    
    def reports_by_metric(self, begin=None, end=None):
        """agrupa reportes en un diccionario de metricas

        Returns:
            list: lista de tuplas conteniendo metricas y  un queryset de reportes
        """   
        rbm = []
        query = {}
        if begin:
            query['begin'] = begin
        if end:
            query['end'] = end

        if self.company:
            query['company'] = self.company
        # for metric in self.metrics.all():
        #     if metric.tipo == 'A':
        #         rbm.append( (metric, qs.filter(metric=metric)) )
        #     if metric.tipo == 'E' or  metric.tipo == 'C':
        #         rbm.append( ( metric, None ) )
        cprint(query, 'white', 'on_blue')
        for metric in self.metrics.all():
            rbm.append((metric,metric.reports(**query)))
        
        return rbm
    
    # def get_reports_between(self, begin, end):
    #     filters = {
    #         'begin':begin, 
    #         'end':end
    #     }
    #     if self.company:

    #     reports = []
    #     for metric in self.metrics.all():
    #         reports.append(metric.reports(**filters))
    # ---------------------------------
    #  Reports
    # ----------------------------------
    def get_reports(self,**kwargs):


        cprint(kwargs, 'white', 'on_cyan')
        reports = [m[1] for m in self.reports_by_metric(**kwargs)]
        return reduce(lambda x,y:x|y, reports )

    def all_reports(self,begin=None, end=None):
        # Retorna un QS base parabuscar reportes asociados a un indicador, 
        # que puede ser de una empresa o no
        # TODO: aqui podemos agregar que sean indicadores asociados a  un lot+
        query = {}
        if begin:
            query['begin'] = begin
        if end:
            query['end'] = end
        
        import pdb; pdb.set_trace()

        reports = [m[1] for m in self.reports_by_metric(**query)]
        return reduce(lambda x,y:x|y, reports )

        # metrics = self.metrics.all()
        # reports=[]
        # for metric in self.metrics.all():
        #     reports.append(metric.reports(company=self.company))

        # company = self.company
        # filters = {
        #     'metric__in':metrics,
        # }
        
        # if company is not None:
        #     filters['company'] = company
        
        # reports = Report.objects \
        #     .filter(**filters) \
        #     .filter(~ Q(value = None))
        # return reports
    

    def total_reports(self):
        return self.all_reports().count()
    
    def total_metrics(self):
        return self.metrics.count()


    # def get_reports_between(self, begin, end):
    #     filters = {
    #         'begin':begin, 
    #         'end':end
    #     }
    #     if self.company:
    #         query['company'] = self.company

    #     reports = []
    #     for metric in self.metrics.all():
    #         reports.append(metric.reports(**filters))

    
    # def days_list(self, begin, end):
    #     if begin.__class__ == datetime:
    #         begin = begin.date()
    #     if end.__class__ == datetime:
    #         end = end.date()

    #     total_days= (end - begin).days + 1
    #     return [ begin + timedelta(days=i) for i in range(total_days) ]

    # def days_covered(self, qs):
    #     days_by_report = [self.days_list(r.begin, r.end) for r in qs]
    #     covered_days = []
    #     for dl in days_by_report:
    #         covered_days = covered_days + dl
    #     return covered_days
    
    # def mising_dates(self, qs, begin, end):
    #     tocover = self.days_list(begin,end)
    #     covered = self.days_covered(qs)
    #     return [d for  d in tocover if  d not in covered]

    # def overlaped_dates(self, qs):
    #     covered = self.days_covered(qs)
    #     return {d for d in covered if covered.count(d) > 1 }
    
    def get_informe(self, begin, end, period = None):
        return Informe(begin, end, self, period)
    
    # ---------------------------------
    #  Metas
    # ----------------------------------    
        
    @property
    def active_goals(self):
        ''' Optiene los reportes asociados a el indicador especifico'''
        return self.goals.filter(completed=False)

    @property
    def total_active_goals(self):
        ''' Optiene los reportes asociados a el indicador especifico'''
        return self.active_goals.count()

    @property
    def completed_goals(self):
        ''' Optiene los reportes asociados a el indicador especifico'''
        return self.goals.filter(completed=True)

    @property
    def recent_goals(self):
        ''' Optiene los reportes asociados a el indicador especifico'''
        return self.goals \
            .filter(completed=False) \
            .order_by('-end')[:3]


    # #----------------------------------
    #  Result procesing
    # ----------------------------------

    # def reports_by_metric(self):
    #     """agrupa reportes en un diccionario de metricas

    #     Args:
    #         qs (Queryset): reportes en base de datos filtrados por los parametros definidos.

    #     Returns:
    #         dict: diccionario que organiza los reportes por nombre de la metrica
    #     """   
    #     rbm = []
    #     # for metric in self.metrics.all():
    #     #     if metric.tipo == 'A':
    #     #         rbm.append( (metric, qs.filter(metric=metric)) )
    #     #     if metric.tipo == 'E' or  metric.tipo == 'C':
    #     #         rbm.append( ( metric, None ) )
    #     for metric in self.metrics.all():
    #         rbm.append((metric,metric.reports))
        
    #     return rbm


    def get_callback(self, metric_dict):
        """obtener y utilizar el callback de procesamiento de reportes para generar determinado indicador   

        Args:
            metric_dict (dict): [diccionario de metricas con la lista de dias]

        Returns:
            int: retorna un valor que es el resultado del procesamitno de los valores de las metricas
        """        
        # self.type 
        # Asumiremos por agora que todos 
        # los indicadores son simples
        components = { c.role: c.metrica.name for c in self.components.all() }
        if self.tipo == 'A':
            name = self.metrics.all()[0].name
            return PCallbacks('Simple')(metric_dict, name)

        elif self.tipo == 'C':
            return PCallbacks('Cociente')(metric_dict,  components)


        elif self.tipo == 'E':
            return PCallbacks('Estado')(metric_dict,  components)
        
        elif self.tipo == 'P':
            return PCallbacks('Porcentaje')(metric_dict,  components)
        
        elif self.tipo == 'SA':
            return PCallbacks('Producto')(metric_dict,  components)

        name = self.metrics.all()[0].name
        return PCallbacks('Simple')(metric_dict, name)


    def days_by_metric(self, qs, dayrange):
        """dias a reportar divididos entre metricas

        Args:
            qs (Queryset): reportes en base de datos filtrados por los parametros definidos.
            dayrange (tuple): fecha de inicio y fecha de finaliación

        Returns:
            dict: diccionario que separa el listado de dias de reporte entre las distintas metricas por nombre
        """ 
        days_by_metric = {}
        for metric in self.metrics.all():
            days_by_metric[metric.name] = metric.results_by_day(dayrange, company=self.company)
        # for metric, reportsqs in self.reports_by_metric(qs):
        #     if metric.tipo == 'A':
        #         days_by_metric[metric.name] = self.divide_in_days(reportsqs, dayrange)
        #     elif metric.tipo == 'E' or metric.tipo == 'C':
        #         days_by_metric[metric.name] = self.fill_state_days(metric,dayrange) 
        return days_by_metric

    
    # def fill_state_days(self, metric, dayrange):
    #     """queryset a dias

    #     Args:
    #         metric (Queriset): una metrica especifica
    #         dayrange (tuple): rango de dias esperados

    #     Returns:
    #         list: lista de diccionarios con los dias con la constante del los valores expresada casa dia
    #     """
    #     begin = dayrange[0]
    #     constants_in_time= Report.objects.filter(metric=metric, begin__lte=begin).order_by('begin')
    #     constant_index = 0
    #     dias = self.days_list(dayrange[0], dayrange[1])
    #     diascovered = []
    #     # import pdb; pdb.set_trace()
    #     for dia in dias:
    #         constant = constants_in_time[constant_index]
    #         if constant.end > dia:
    #             constant_index = constant_index + 1
    #         diascovered.append({ 'date':dia,'value':constant.value })
    #     return diascovered
             





    # def divide_in_days(self, qs, dayrange):
    #     """queryset a dias

    #     Args:
    #         qs (Queriset): listado de reportes filtrados que cumplen con las variables (tiempos de inicio y finalizacion etc)
    #         dayrange (tuple): fecha de inicio y fecha de finalizacón

    #     Returns:
    #         list: lista de diccionarios con los valores por dia calculados dividiendo el valor de los repoirtes que represerntan a mas de un dia entre el numero de dias que representan y el dia al que represetan.
    #         La lista de dias incluye a los dias sin reporte por que es el total de dias a reportar
    #     """        #
    #     diasnull = self.mising_dates(qs,dayrange[0],dayrange[1])
    #     diascovered = []
    #     for report in qs:
    #         try:
    #             desagregated_value = report.value / report.days
    #         except Exception as e:
    #             print(e)
    #             import pdb; pdb.set_trace()
    #         diascovered = diascovered +[{ 'date':d,'value':desagregated_value } for d in self.days_covered([report])]
    #     diascovered = diascovered + [{ 'date':d,'value':0 } for d in diasnull]
    #     return diascovered


class Goal(models.Model):
    name = models.CharField(blank=True, max_length=250)
    indicator = models.ForeignKey(
        Indicator,
        related_name="goals", 
        on_delete=models.CASCADE)
    group = models.CharField(max_length=50, 
        null=True,
        blank=True)
    begin = models.DateField()
    end = models.DateField()
    # Data de la meta
    goal  = models.IntegerField()
    fail  = models.CharField(
        max_length=50,
        null=True, 
        blank=True)
    reverse = models.BooleanField(default=False)

    # Resultados calculados
    result = models.IntegerField(null=True)
    completed = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'

    @property
    def duration(self):
        return (self.end - self.begin).days -1 


    @property
    def period(self):
        beg = self.begin.strftime('%d %B %Y')
        end = self.end.strftime('%d %B %Y')
        return f'Desde {beg} hasta {end}'

    
    @property
    def inform(self):
        return self.indicator.get_informe(self.begin, self.end, 1)

    @property
    def reports(self):
        return self.inform.reports

    @property
    def report_rate(self):
        return self.inform.delivery_rate

    @property
    def computed_result(self):
        return self.inform.val_agregated


    @property
    def daily_avg(self):
        daily = self.inform.val_in_periods
        values = [d for d in daily]
        # total_reported = reduce(lambda x,y:x+y,values)
        return  Decimal(self.computed_result / len(daily)).quantize(Decimal('.01'),rounding=ROUND_UP)

    @property
    def expected(self):
        # import pdb; pdb.set_trace()
        return self.daily_avg * self.inform.total_days_to_report


    @property
    def status(self):
        try:
            medium = int(self.fail.split(',')[0])
        except Exception as e:
            print(e)
            medium = self.goal
        
        result = 'good'
        if not self.reverse:
            if self.expected >= self.goal:
                return  result

            if self.expected < self.goal:
                result = 'medium'

            if self.expected < medium:
                result = 'bad'
        else:

            if self.expected < medium:
                return  result

            if self.expected < self.goal:
                result = 'medium'

            if self.expected >= self.goal:
                result = 'bad'

        return  result

    @property
    def chart(self):
        size = round(self.duration / 10)
        inform = self.indicator.get_informe(self.begin, self.end, size)
        return inform.call_val_in_periods(method="A")

    @property
    def variance_chart(self):
        size = round(self.duration / 10)
        inform = self.indicator.get_informe(self.begin, self.end, size)
        return inform.call_val_in_periods(method="V")

    @property
    def acomplishment(self):
        return Decimal(self.computed_result/self.goal).quantize(Decimal('.01'),rounding=ROUND_UP)    

    def complete(self):
        '''
            Guarda los reultados de los reportes, 
            y coloca este periodo como cerrado
        '''
        # TODO: Aqui hay que verificar si los 
        # resultados computados cubren todo un 
        # periodo
        self.reports.update(editable=False)
        self.results = self.computed_result
        self.completed=True
        self.save()
        return self

    def reopen(self):
        '''
            Reabre la posibilidad 
            de cambiar resutados
        '''
        self.reports.update(editable=True)
        self.results = None
        self.completed = False
        self.save()
        return self


    def __str__(self):
        return f'{self.period}:{self.acomplishment*100}%'    
