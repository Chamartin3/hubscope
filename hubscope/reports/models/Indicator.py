from .Metric import Metric
from .Company import Company, Position
from .Reports import Report
from .ProcesingCallbacks import procesing as PCallbacks

import calendar 
from django.db import models
from datetime import  datetime, timedelta
from django.utils.timezone import localdate
from hubscope.accounts.models import User

from django.core.exceptions import ValidationError
from django.core.validators import int_list_validator
from functools import reduce
from termcolor import cprint


class Informe:
  
    def __init__(self, b, e, indicator, period_size=None):
        self.begin = b
        self.end = e
        self.indicator = indicator
        self.period_size = period_size

    def __str__(self):
        return f'{self.period_txt} (periods:{self.period_size}) {self.indicator}'

    @property
    def daily_rbm(self):
        """ metricas con un listado de dia.
        cada metrica contiene una lista con todos los dias que conforman el periodo del informe

        ada dia es un diccionario que contiene:
            - la fecha
            - el valor: calculado de la metica (si viene de un reporte que es mas de un dia es la porcion de ese dia)

        Returns:
            dict: diccionario de metricas que cotienen listas de reportesdias (dict)
        """           
        return self.indicator.days_by_metric(self.reports, self.dayrange) 

    @property
    def reports(self):
        """Reoprtes que conforman este informe

        Returns:
            list: listado de reportes que estan dentro del rango de fechas del informe
        """        
        return self.indicator.get_reports_between(self.begin,self.end)

    @property
    def mising(self):
        """reportes faltantes

        Returns:
            list: lista de fechas donde no hay reportes de esta metricas
        """ 
        return self.indicator.mising_dates(self.reports, self.begin, self.end)

    @property
    def overlaped(self):
        """detecta los dias donde hay solapamiento de reportes

        Returns:
            list: lista de fechas donde hay solapamiento
        """        
    
        return list(self.indicator.overlaped_dates(self.reports))

    @property
    def dayrange(self):
        return (self.begin,self.end)

    @property
    def begin(self):
        return self._begin
    @begin.setter
    def begin(self, val):
        self._begin = val.date() if val.__class__ == datetime else val

    @property
    def end(self):
        return self._end
    @end.setter
    def end(self, val):
        self._end = val.date() if val.__class__ == datetime else val


    @property
    def period_size(self):
        return self._period_size
    @period_size.setter
    def period_size(self, value=None):
        if value is None:
            self._period_size =(self.end - self.begin).days +1
        else:
            self._period_size = value

    @property
    def period_txt(self):
        return f"{self.begin.strftime('%d/%m/%y')}-{self.end.strftime('%d/%m/%y')}"
    
    @property
    def periods(self):
        period_size = self.period_size
        begindate = self.begin
        enddate =self.end
        periods = []
        while True:
            if begindate > enddate:
                break
            
            refend = begindate + timedelta(days=period_size-1)
            if refend >= enddate:
                periods.append((begindate,enddate))
                break
            periods.append((begindate,refend))

            begindate = begindate + timedelta(days=period_size)
        return periods

    def filter_metrics_between(self, reportlist, begin, end):
        # import pdb; pdb.set_trace()
        return [ r for r in reportlist if begin <= r['date'] <= end ]

    def agregate_in_periods(self, dailymetrics):
        periodresults = []
        for period in self.periods:
            b = period[0]
            e = period[1]
            name = f"{b.strftime('%d/%m/%y')}-{e.strftime('%d/%m/%y')}"
            mperiodreports = { n:self.filter_metrics_between(m,b,e) for n,m in dailymetrics.items() }
            periodresults.append({ name: self.indicator.get_callback(mperiodreports)})
        return periodresults
        # Hay que agregar una especie de objero que llame a un callback con las metricas

    def val_agregated(self):
        return self.indicator.get_callback(self.daily_rbm)


    def val_in_periods(self):
        # periods = self.generate_periods(self.period_size,self.dayrange)
        # dailymetrics = self.days_by_metric(qs, self.dayrange)
        return self.agregate_in_periods(self.daily_rbm)
    
    def cli_briefing(self):
        cprint(f'Period: {self.begin.strftime("%d%b-%Y")} - {self.end.strftime("%d%b-%Y")}','cyan')
        # cprint(self.indicator.metric.name, 'cyan' ) 
        cprint(f'Reports:{len(self.reports)}', 'cyan')

        if len(self.mising) > 0:
            cprint(f'Mising:{len(self.mising)}', 'red')
            print(self.mising)
        else:
            print('---- Completed days -----')

        if len(self.overlaped) > 0:
            cprint(f'Overlaped:{len(self.overlaped)}', 'red')
            print(self.overlaped)
        else:
            print('---- No overlaps -----')

class Indicator(models.Model):
    '''
        Define las unidades de medida compuestas por uno 
        o mas metricas de una compañia, asi como una meta  para un periodo especifico
    '''
    ITYPES =(
        ('S','Simple' ),
        ('R','Rango'),
        ('P','Porcentaje'),
        ('E', 'Especial')
    ) 
    name = models.CharField(blank=True, max_length=100)
    unidad = models.CharField(max_length=50)
    desc = models.TextField()
    tipo = models.CharField(choices=ITYPES, max_length=2)
    active = models.BooleanField(default=True)
    metrics = models.ManyToManyField(Metric, 
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
    

    # ---------------------------------
    #  Reports
    # ----------------------------------
    @property
    def all_reports(self):
        # Retorna un QS base parabuscar reportes asociados a un indicador, 
        # que puede ser de una empresa o no
        # TODO: aqui podemos agregar que sean indicadores asociados a  un lote
        metrics = self.metrics.all()
        company = self.company
        filters = {
            'metric__in':metrics,
        }
        
        if company is not None:
            filters['company'] = company
        
        reports = Report.objects \
            .filter(**filters)
        return reports
    
    def total_reports(self):
        return self.all_reports().count()
    
    def total_metrics(self):
        return self.metrics.all().count()

    def get_reports_between(self, begin, end):
        filters = {
            'begin__gte':begin, 
            'end__lte':end
        }
        return self.all_reports.filter(**filters)
    
    def days_list(self, begin, end):
        if begin.__class__ == datetime:
            begin = begin.date()
        if end.__class__ == datetime:
            end = end.date()

        total_days= (end - begin).days + 1
        return [ begin + timedelta(days=i) for i in range(total_days) ]

    def days_covered(self, qs):
        days_by_report = [self.days_list(r.begin, r.end) for r in qs]
        covered_days = []
        for dl in days_by_report:
            covered_days = covered_days + dl
        return covered_days
    
    def mising_dates(self, qs, begin, end):
        tocover = self.days_list(begin,end)
        covered = self.days_covered(qs)
        return [d for  d in tocover if  d not in covered]

    def overlaped_dates(self, qs):
        covered = self.days_covered(qs)
        return {d for d in covered if covered.count(d) > 1 }
    
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
    def completed_goals(self):
        ''' Optiene los reportes asociados a el indicador especifico'''
        return self.goals.filter(completed=True)

    @property
    def recent_goals(self):
        ''' Optiene los reportes asociados a el indicador especifico'''
        return self.goals \
            .filter(completed=False) \
            .order_by('-end')[:5]


    # #----------------------------------
    #  Result procesing
    # ----------------------------------

    def reports_by_metric(self, qs):
        """agrupa reportes en un diccionario de mmetricas

        Args:
            qs (Queryset): reportes en base de datos filtrados por los parametros definidos.

        Returns:
            dict: diccionario que organiza los reportes por nombre de la metrica
        """        
        rbm = {}
        for metric in self.metrics.all():
            rbm[ metric.name ] = qs.filter(metric=metric)
        return rbm


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
        # if self.tipo == 'S':
        #     pass
        name = self.metrics.all()[0].name
        return PCallbacks('Simple')(metric_dict, name)


    def days_by_metric(self, qs, dayrange):
        """dias a reortar divididos entre metricas

        Args:
            qs (Queryset): reportes en base de datos filtrados por los parametros definidos.
            dayrange (tuple): fecha de inicio y fecha de finaliación

        Returns:
            dict: diccionario que separa el listado de dias de reporte entre las distintas metricas por nombre
        """        
        return { name:self.divide_in_days(qs,dayrange) for name, qs in self.reports_by_metric(qs).items() }

    def divide_in_days(self, qs, dayrange):
        """queryset a dias

        Args:
            qs (Queriset): listado de reportes filtrados que cumplen con las variables (tiempos de inicio y finalizacion etc)
            dayrange (tuple): fecha de inicio y fecha de finalizacón

        Returns:
            list: lista de diccionarios con los valores por dia calculados dividiendo el valor de los repoirtes que represerntan a mas de un dia entre el numero de dias que representan y el dia al que represetan.
            La lista de dias incluye a los dias sin reporte por que es el total de dias a reportar
        """        #
        diasnull = self.mising_dates(qs,dayrange[0],dayrange[1])
        diascovered = []
        for rep in qs:
            desagregated_value = rep.value / rep.days
            # import pdb; pdb.set_trace()
            diascovered = diascovered +[{ 'date':d,'value':desagregated_value } for d in self.days_covered([rep])]
        diascovered = diascovered + [{ 'date':d,'value':0 } for d in diasnull]
        return diascovered

    # def generate_periods(self, period_size, day_range):
    #     begindate = day_range[0] 
    #     enddate = day_range[1]
    #     periods = []
    #     while True:
    #         if begindate > enddate:
    #             break
            
    #         refend = begindate + timedelta(days=period_size-1)
    #         if refend >= enddate:
    #             periods.append((begindate,enddate))
    #             break
    #         periods.append((begindate,refend))

    #         begindate = begindate + timedelta(days=period_size)
    #     return periods

    # def agregate_in_periods(self, periods, dailymetrics):
    #     periodresults = []
    #     for period in periods:
    #         b = period[0]
    #         e = period[1]
    #         name = f"{b.strftime('%d/%m/%y')}-{e.strftime('%d/%m/%y')}"
    #         periodreports = [m for m in dailymetrics if b>=dailymetrics['date'] >=e ]
    #         periodresults.append({ name: self.get_callback(periodreports)})
    #     return periodresults
    #     # Hay que agregar una especie de objero que llame a un callback con las metricas

    # def agregated_results(self, qs, dayrange):
    #     dailymetrics = self.days_by_metric(qs,dayrange)
    #     return self.get_callback(dailymetrics)


    # def period_results(self, qs, dayrange, size = 7):
    #     periods = self.generate_periods(size,dayrange )
    #     dailymetrics = self.days_by_metric(qs,dayrange)
    #     return self.agregate_in_periods(periods , dailymetrics)

            

class Goal(models.Model):
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
        validators=[int_list_validator],
        null=True, 
        blank=True)
    


    # Resultados calculados
    result = models.IntegerField(null=True)
    completed = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'

    @property
    def duration(self):
        return (self.end - self.begin).days


    @property
    def period(self):
        beg = self.begin.strftime('%d %B %Y')
        end = self.end.strftime('%d %B %Y')
        return f'Desde {beg} hasta {end}'

    @property
    def calculated_results(self):    
        ''' optiene los resutados de los reportes 
            solo si los la instancia no tiene reultados
        '''
        if self.completed:
            return self.results
        return self.compute_results      

    @property
    def acomplishment(self):
        return self.compute_results/self.goal   
    
    @property
    def reports(self):
        return self.get_reports()


    def get_reports(self):
        '''
            optiene los reportes de un periodo especifico
        
        '''
        metrics = self.indicator.metrics.all()
        company = self.indicator.company
        filters = {
            'metric__in':metrics,
            'begin__gte':self.begin, 
            'end__lte':self.end
        }
        if company is not None:
            filters['company'] = company
        reports = Report.objects \
            .filter(**filters)
        
        # TODO: Hay que trabajar que hacer en el caso de que
        # el indicaodr contenga mas de una metrica por que
        #  hay la psibilidad de que debas nser procesadas 
        # por periodo (Por ahora suponemos una sola metrica 
        # por indicador
        return reports

    def compute_results(self):
        '''
            Optiene los reusutados con base en los reportes
        '''
        reports_values=[r.value for r in self.reports]
        # Aqui el resultado siempre es na suma y no se 
        # considera mas de una metrica
        return reduce((lambda x, y: x + y), reports_values)


    def complete(self):
        '''
            Guarda los reultados de los reportes, 
            y coloca este periodo como cerrado
        '''
        # TODO: Aqui hay que verificar si los 
        # resultados computados cubren todo un 
        # periodo 
        self.results=self.compute_results
        self.completed=True
        return self.save()  

    def reopen(self):
        '''
            Reabre la posibilidad 
            de cambiar resutados
        '''
        self.results = None
        self.completed = False
        return self.save()


    def __str__(self):
        return f'{self.period}:{self.acomplishment}'    
