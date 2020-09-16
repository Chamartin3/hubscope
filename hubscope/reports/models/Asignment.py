from .Metric import Metric
from .Company import Company, Position
from .Reports import Report
# from .Indicator import Indicator, Goal

import calendar 
from django.db import models
from datetime import  datetime, timedelta, date
from django.utils.timezone import localdate
from hubscope.accounts.models import User

from django.core.exceptions import ValidationError
from django.core.validators import int_list_validator
from functools import reduce

from termcolor import cprint
import pdb
# Create your models here.
  


class Asignment(models.Model):
    '''
        cada cuanto se reporta una metrica
        fecuencia en dias/mensualmente
    '''
    # Report Data
    metric = models.ForeignKey(Metric, 
        on_delete=models.CASCADE)
    # Responsaible
    company = models.ForeignKey(Company, 
        on_delete=models.CASCADE, 
        related_name='expected_reports')


    
    # Crea tareas periodicamente si es verdadero, 
    # si es null elimina la tarea despues cumplida  por que es one time
    periodic = models.NullBooleanField(default=True)
    
    # Ulima entrega/ periodo de inicio
    last_begin = models.DateField(blank=True, default=localdate)
    last_end = models.DateField()
    

    # dias para entregar
    days_to_deliver = models.IntegerField()
    # Reportes autogenerados
    genetated_reports = models.ManyToManyField('Report', related_name='asignment')
    
    # cALCULO DE FECHAS
    FREC_TYPE=(
        ('MONT','Mensual'),
        # ('QUIN','Quincenal'),
        ('WEEK','Semanal'),
        ('DAY','Diario'),
        ('OT','OneTime'),
    )
    frecuency = models.CharField(choices=FREC_TYPE, max_length=50, default='OT')
    metafreq = models.CharField(max_length=50, validators=[int_list_validator], blank=True, null=True)

    class Meta:
        verbose_name = "Asignment"
        verbose_name_plural = "Asignments"

    @property
    def total_genetated_reports(self):
        return self.genetated_reports.count()

    @property
    def first_report(self):
        return self.genetated_reports.first()
    
    @property
    def first_report_date(self):
        return self.first_report.begin

    @property
    def reports_by_status(self):
        bystatus ={}
        for rep in self.genetated_reports.all():
            st = bystatus.get(rep.status, None)
            if st:
                bystatus[rep.status] = st + 1
            else:
                bystatus[rep.status] = 1
        return bystatus



    @property
    def target_days(self):
        '''
             Dias involucrados en la tarea, 
             -si es diaria retorna el numero de dias hasta la proxima
             -si es semanal retorna los numeros de dia de la semana
             -si es mensual retorna los numeros del dia en el mes
        '''
        if self.metafreq is None:
            return None 
        days =  [int(n) for n in self.metafreq.split(',')]
        days.sort()
        return days 

    def daily_frequency(self):
        if self.target_days:
            return self.target_days[0] - 1 
        return 0

    def weekly_frequency(self, begin):
        actual_weekday = begin.weekday()
        weekdays = self.target_days
        # weekdays = [ int(c) for c in self.target_days ]
        # weekdays.sort()
        next_weekday = next((wd for wd in weekdays if wd >= actual_weekday), min(weekdays)) 
        next_weekday = next_weekday + 1
        actual_wd = actual_weekday + 1
        if next_weekday > actual_wd:
            return next_weekday - actual_wd
        else:
            return (7 - actual_wd) + next_weekday

    def monthly_frequency(self, begin):
        
        if not self.target_days:
            mes = begin.month + 1
            dia = begin.day
        else:
            # monthdays = [int(c) for c in self.target_days]
            # monthdays.sort()
            # import pdb; pdb.set_trace()
            monthdays = self.target_days
            dia = next((wd for wd in monthdays if wd >= begin.day+1), min(monthdays))
            mes = begin.month 
            if dia < begin.day:
                mes = mes + 1
        ano = begin.year
        if mes > 12:
            mes = 1
            ano = ano + 1

        monthlimit = calendar.monthrange(ano, mes)[1]
        if dia > monthlimit:
            dia = monthlimit

        try:
            nextdate = date(day=dia, month=mes, year=ano)
           
        except Exception as identifier:
            import pdb; pdb.set_trace()
        return (nextdate-begin).days


    def days_util_next(self, begin):
        '''
        Calcula el numero de dias faltantes para la proxima fecha limite
        
        '''
        if self.frecuency == 'DAY':
            return self.daily_frequency()

        if self.frecuency == 'WEEK':
            return self.weekly_frequency(begin)

        if self.frecuency == 'MONT':
            return self.monthly_frequency(begin)

    def next_end(self, begin=None):
        '''
            Genera el la proxima fecha de cierre, basandonos en un inicio esblecido
        '''

        if begin is None:
            begin = localdate()
        days = self.days_util_next(begin)
        cprint(days, 'white','on_blue')
        return begin + timedelta(days)
    
    @property
    def next_ocurrence(self):
        if self.last_end:
            return self.last_end + timedelta(1)
        return self.next_end(self.last_begin) + timedelta(1)


    def generate_report(self, begin, end, deadline=None):
        # end = self.next_end(begin)
        # Chec the  existance of report
        dl = deadline if deadline is not None else self.get_deadline_date(end)
        cprint(begin, 'white','on_green')
        cprint(end, 'white','on_green')
        rep, created = Report.objects.get_or_create(
            company=self.company,
            metric=self.metric,
            begin=begin,
            end=end,
            defaults={'deadline':dl,}
        )
        if created:
            self.genetated_reports.add(rep)
        return rep

    def filled_report(self):
        if self.frecuency != "OT":
            self.delete()
            return True
        self.check_state()



    def get_deadline_date(self, end):            
        native_deadline =  end + timedelta( self.days_to_deliver +1 )
        if native_deadline > localdate():
            return native_deadline
        return localdate() + timedelta( self.days_to_deliver +1 )

    def check_state(self):
        if self.next_ocurrence <= localdate():
            new_begin = self.next_ocurrence 
            new_end = self.next_end(self.next_ocurrence)
            self.generate_report(new_begin, new_end)
            self.last_begin = new_begin
            self.last_end = new_end
            self.check_state()
        return True

    
    def __str__(self):
        return f'{self.metric} every {self.frecuency} days'

    def save(self, *args, **kwargs):
        if self.periodic:
            self.last_end = self.next_end(self.last_begin) 
        super().save(*args, **kwargs)
        self.generate_report(self.last_begin, self.last_end)
        self.check_state()
        return self