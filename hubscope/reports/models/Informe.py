
from .utils import DayRange
from datetime import datetime, timedelta
from decimal import ROUND_UP, Decimal
from termcolor import cprint

class Informe:
  
    def __init__(self, b, e, indicator, period_size=None):
        self.begin = b
        self.end = e
        self.dayrange = DayRange(b,e)
        self.indicator = indicator
        self.company = indicator.company
        # import pdb; import pdb; pdb.set_trace()
        self.period_size = period_size
        self.__set_sumary__()


    def __str__(self):
        return f'{self.period_txt} (periods:{self.period_size}) {self.indicator}'


    def __set_sumary__(self):
        self.days_to_report = self.dayrange.days
        self.total_days_to_report = self.dayrange.size
        missing = []
        overlaped = {}
        total_overlaped = 0

        for metric in self.indicator.metrics.all():
            msumary = metric.days_reported(self.dayrange, self.company)
            overlaped[metric.name] = list(msumary['overlaped'])
            total_overlaped = total_overlaped + len(msumary['overlaped'])

            missing = missing + msumary['missing']
        
        self.missing = list( set(missing) )
        self.total_mising = len(missing)

        self.total_overlaped = total_overlaped
        self.overlaped = overlaped

        self.reported_days = self.dayrange.size - self.total_mising

    @property
    def reports(self):
        """Reoprtes que conforman este informe

        Returns:
            list: listado de reportes que estan dentro del rango de fechas del informe
        """        
        return self.indicator.get_reports(begin=self.begin,end=self.end)

    @property
    def total_reports(self):
        return  self.reports.filter(metric__tipo__in=['E','A']).count()
    

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
        cprint('RBM','red')
        days_by_metric = {}
        for metric in self.indicator.metrics.all():
            days_by_metric[metric.name] = metric.results_by_day(
                                                self.dayrange, 
                                                company=self.company
                                            )
        return days_by_metric
        # return self.indicator.days_by_metric(self.reports, self.dayrange, company=self.company) 




    #------------------------------------
    # Sumary
    # --------------------------------
    # # To Cover
    # @property
    # def days_to_report(self):
    #     return (self.end - self.begin).days + 1

    # # Missing
    # @property
    # def mising(self): 
    #     return self.indicator.mising_dates(self.reports, self.begin, self.end)
    # @property
    # def total_mising(self):
    #     return len(self.mising)        
    
    # # Overlaped
    # @property
    # def overlaped(self):
    #     return list(self.indicator.overlaped_dates(self.reports))
    # @property
    # def total_overlaped(self):
    #     return len(self.overlaped)    

    # # Covered
    # @property
    # def reported_days(self):
    #     return self.days_to_report-self.total_mising


    @property
    def delivery_rate(self):
        return (self.reported_days / self.dayrange.size ) *100
    # @property
    # def dayrange(self):
    #     # return (self.begin,self.end)
    #     return DayRange(self.begin,self.end)

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
        if int(value) < 1:
            value = 1
        if value is None or value == '':
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
                    var = 1
                    if value != 0:
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
