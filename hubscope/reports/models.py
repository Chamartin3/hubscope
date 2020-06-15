import calendar 
from django.db import models
from datetime import  datetime
from django.utils.timezone import localdate
from hubscope.accounts.models import User
from .managers import ReportsManager
from django.core.exceptions import ValidationError
from django.core.validators import int_list_validator
from functools import reduce

# Create your models here.



class Company(models.Model):
    '''
        Cada una de las empresas, Unidad basica de organización dde informes y reportes
    '''
    name = models.CharField(blank=True, max_length=100)
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companys"
    def __str__(self):
        return f'{self.name}'

class Position(models.Model):
    """Es la forma en la que se relaciona los accesos y los usuarios a los reportes"""
    person = models.ForeignKey(User,
        on_delete=models.CASCADE, 
        related_name='roles'
    )    
    company = models.ForeignKey(Company,
        on_delete=models.CASCADE, 
        related_name='members'
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        """Unicode representation of CompanyRole."""
        return f'{self.name} en {self.company}: {self.person}'


class Metric(models.Model):
    '''
        Indicador Reportado   
    '''
    TIPOS = [
        ('C','Cuantitativo'),
        ('Q','Cualitativo')
    ]
    name = models.CharField(unique=True, max_length=100)
    tipo = models.CharField(choices=TIPOS, blank=True, max_length=100)
    unidad = models.CharField(max_length=50, blank=True)
    desc = models.TextField()

    class Meta:
        verbose_name = "Metric"
        verbose_name_plural = "Metrics"
        
    def __str__(self):
        return f'{self.name} {self.tipo}'

    def reports(self, **kwargs):
        ''' Optiene los reportes de una metrica especifica'''
        query={}
        import pdb; pdb.set_trace()
        for k,v in kwargs.items():
            if k == 'begin':
                query['begin__gte'] = v
            elif k == 'end':
                query['end__lte'] = v
            else:
                query[k] = v

        return self.responses.filter(**query)

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
    deadline=models.DateField(blank=True, null=True)
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

    objects=ReportsManager()

    
    def clean(self):
        if self.begin > self.end:
            raise ValidationError("La fecha fecha de inicio no puede ser posterior a la fecha de finalización")

    def save(self, *args, **kwargs):
        self.full_clean()
        fist_time = self.created_at is None
        if self.value is not None and fist_time:
            self.created_at = localtime()
        return super().save(*args, **kwargs)

    @property
    def value(self):
        m = self.metric
        if m.tipo == 'C':
            return self.num_value
        return self.text_value

    @property
    def days(self):
        return (self.end-self.begin).days

    def __str__(self):
        """Unicode representation of Response."""
        return f'{self.metric}({self.created_at}): {self.value}'




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

    @property
    def active_periods(self):
        ''' Optiene los reportes asociados a el indicador especifico'''
        return self.periods.filter(completed=False)

    @property
    def completed_periods(self):
        ''' Optiene los reportes asociados a el indicador especifico'''
        return self.periods.filter(completed=True)

    @property
    def recent_periods(self):
        ''' Optiene los reportes asociados a el indicador especifico'''
        return self.periods \
            .filter(completed=False) \
            .order_by('-end')[:5]

    

class Goal(models.Model):
    indicator = models.ForeignKey(
        Indicator,
        related_name="periods", 
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
        metrics=self.indicator.metrics.all()
        company=self.indicator.company
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


class Asignment(models.Model):
    '''
        cada cuanto se reporta una metrica
        fecuencia en dias/mensualmente
        TODO: Definir tipos de periodicidad (Quincenal, Mensual, etc)
    '''
    metric = models.ForeignKey(Metric, 
        on_delete=models.CASCADE)
    company = models.ForeignKey(Company, 
        on_delete=models.CASCADE, 
        related_name='expected_reports')
    
    periodic = models.NullBooleanField(default=True)
    # Crea tareas periodicamente si es verdadrro, 
    # si es null elimina la tarea despues cumplida  por que es one time
    
    last = models.DateField(blank=True)
    # Ulima entrega/ periodo de inicio

    deliver_time = models.IntegerField()
    # dias para entregar
    
    FREC_TYPE=(
        ('MONT','Mensual'),
        # ('QUIN','Quincenal'),
        ('WEEK','Semanal'),
        ('DAY','Diario'),
    )

    frecuency = models.CharField(choices=FREC_TYPE, max_length=50)
    metafreq = models.CharField(max_length=50, validators=[int_list_validator], blank=True, null=True)

    class Meta:
        verbose_name = "Asignment"
        verbose_name_plural = "Asignments"

    @property
    def days_to_next(self):

        begining = localdate() if self.last is None else self.last 
        meta =  None if self.metafreq is None else self.metafreq.split(',')

        if self.frecuency == 'DAY':
            if meta is None:
                return 1
            return int(meta[0])

        if self.frecuency == 'WEEK':
            actual_weekday = begining.weekday()
            weekdays = [int(c) for c in meta].sort()
            next_weekday = next((wd for wd in weekdays if wd >= actual_weekday), min(weekdays)) 

            next_weekday = next_weekday + 1
            actual_weekday = actual_weekday + 1
            if next_weekday > actual_wd:
                return next_weekday - actual_wd
            else:
                return (7 - actual_wd) + next_weekday
            
        # if self.frecuency == 'QUIN':
        #     if begining.day <= 15:
        #         day=calendar.monthrange(begining.year, begining.month)
        #         nextdate = datetime.date(day=day, year=begining.year,month=begining.month)
        #     else:
        #         newmonth=begining.month + 1
        #         year = begining.year
        #         if newmonth>12:
        #             year=year+1
        #             newmonth=1
        #         nextdate = datetime.date(day=15, month=newmonth, year=year)
            
        #     return (nextdate-begining).days

        if self.frecuency == 'MONT':
            if meta is None:
                mes = begining.month + 1
                dia = begining.day
            else:
                monthdays = [int(c) for c in meta].sort()
                dia = next((wd for wd in monthdays if wd >= begining), min(monthdays))
                mes = begining.month 
                if dia < begining.day:
                    mes = mes + 1
            ano = begining.year
            if mes>12:
                mes = 1
            ano = ano + 1

            monthlimit = calendar.monthrange(ano, mes)[0]
            if dia>monthlimit:
                mes=monthlimit
            nextdate = datetime.date(day=dia, month=mes, year=ano)

            return (nextdate-begining).days


    @property
    def next_ocurrence(self):
        if self.last is None:
            return localtime.date+datetime.timedelta(self.days_to_next)
        else:
            return self.last+datetime.timedelta(self.days_to_next)


    def __str__(self):
        return f'{self.metric} every {self.frecuency} days'

