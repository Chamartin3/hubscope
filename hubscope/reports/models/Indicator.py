from .Metric import Metric
from .Company import Company, Position
from .Reports import Report
from .ProcesingCallbacks import procesing as PCallbacks

import calendar 
from django.db import models
from django.db.models import Q
from datetime import  datetime, timedelta
from django.utils.timezone import localdate
from hubscope.accounts.models import User
from decimal import ROUND_UP, Decimal

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
    def total_reports(self):
        return len(self.reports)


    @property
    def mising(self):
        """reportes faltantes

        Returns:
            list: lista de fechas donde no hay reportes de esta metricas
        """ 
        return self.indicator.mising_dates(self.reports, self.begin, self.end)
    @property
    def total_mising(self):
        return len(self.mising)        
    
    @property
    def days_to_report(self):
        return (self.end - self.begin).days + 1
    @property
    def reported_days(self):
        return self.days_to_report-self.total_mising
    @property
    def delivery_rate(self):
        return (self.reported_days / self.days_to_report) *100

    @property
    def overlaped(self):
        """detecta los dias donde hay solapamiento de reportes

        Returns:
            list: lista de fechas donde hay solapamiento
        """        
    
        return list(self.indicator.overlaped_dates(self.reports))
    
    @property
    def total_overlaped(self):
        return len(self.overlaped)    

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
            self._period_size = int(value)

    @property
    def period_txt(self):
        if self.begin==self.end:
            return f"{self.begin.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        return f"{self.begin.strftime('%Y-%m-%dT%H:%M:%SZ')}-{self.end.strftime('%Y-%m-%dT%H:%M:%SZ')}"
    
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
        return [ r for r in reportlist if begin <= r['date'] <= end ]

    def agregate_in_periods(self, dailymetrics, method="T"):
        """Agrega los resultados del insdicador en periodos del tamaño establecido

        Args:
            dailymetrics (dict): Diccionario con metricas que contienen listaas de
            maethod (str, optional): Tidpo de aculumulacxcón Defaults to "T".
            T = Total (suma)
            A = Acumulado
            V = Varianza

        Returns:
            list: lista de resultados agregados por periodo
        """        
        periodresults = []
        acumulator=0
        prev = None
        for period in self.periods:
            b = period[0]
            e = period[1]
            name = f"{b.strftime('%d/%m/%y')}-{e.strftime('%d/%m/%y')}"
            # TODO: Crear algo que permita crear una funcion que defina las formas en las que se presnertan las diferencias de cada peridodo, por enmpo Acumulado / Variabilidad
            mperiodreports = { n:self.filter_metrics_between(m,b,e) for n,m in dailymetrics.items() }
            value = self.indicator.get_callback(mperiodreports)
            
            if method == "T":
                periodresults.append({ name: value })
            elif method == "A":
                acumulator=acumulator + value
                periodresults.append({ name: acumulator })
            elif method == "V":
                if prev is None:
                    var = 1
                else:
                    var = prev / value
                periodresults.append({ name: var })
            prev = value

        return periodresults
        # Hay que agregar una especie de objero que llame a un callback con las metricas

    @property
    def val_agregated(self):
        return Decimal(self.indicator.get_callback(self.daily_rbm)).quantize(Decimal('.01'),rounding=ROUND_UP)


    @property
    def val_in_periods(self):
        # periods = self.generate_periods(self.period_size,self.dayrange)
        # dailymetrics = self.days_by_metric(qs, self.dayrange)
        return self.agregate_in_periods(self.daily_rbm) 

    def call_val_in_periods(self, method):
        return self.agregate_in_periods(self.daily_rbm, method) 
    
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
            .filter(**filters) \
            .filter(~ Q(num_value = None))
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
            .order_by('-end')[:3]


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
            try:
                desagregated_value = rep.value / rep.days
            except Exception as e:
                print(e)
                import pdb; pdb.set_trace()
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
        return self.daily_avg * self.inform.days_to_report

    @property
    def status(self):
        try:
            medium = int(self.fail.split(',')[0])
        except Exception as e:
            print(e)
            medium = self.goal
        
        result = 'good'
        if self.expected >= self.goal:
            return  result

        if self.expected < self.goal:
            result = 'medium'

        if self.expected < medium:
            result = 'bad'

        return  result

    @property
    def chart(self):
        size = round(self.duration / 10)
        inform = self.indicator.get_informe(self.begin, self.end, size)
        return inform.call_val_in_periods(method="A")

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
        self.reports.update(editable=False)
        self.results = None
        self.completed = False
        self.save()
        return self


    def __str__(self):
        return f'{self.period}:{self.acomplishment*100}%'    
