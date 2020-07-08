from .Metric import Metric
from .Company import Company, Position
from .Reports import Report
# from .Indicator import Indicator, Goal

import calendar 
from django.db import models
from datetime import  datetime, timedelta
from django.utils.timezone import localdate
from hubscope.accounts.models import User

from django.core.exceptions import ValidationError
from django.core.validators import int_list_validator
from functools import reduce

# Create your models here.
  


class Asignment(models.Model):
    '''
        cada cuanto se reporta una metrica
        fecuencia en dias/mensualmente
    '''
    metric = models.ForeignKey(Metric, 
        on_delete=models.CASCADE)
    company = models.ForeignKey(Company, 
        on_delete=models.CASCADE, 
        related_name='expected_reports')
    
    periodic = models.NullBooleanField(default=True)
    # Crea tareas periodicamente si es verdadero, 
    # si es null elimina la tarea despues cumplida  por que es one time
    

    last = models.DateField(blank=True)
    # Ulima entrega/ periodo de inicio

    delivery_time = models.IntegerField()
    # dias para entregar
    
    # Reporte autogenerado 
    active_report = models.ForeignKey(Report, 
    on_delete=models.SET_NULL,
    related_name='asignment',
    null=True, blank=True)
    next_ocurrence = models.DateField()
    
    FREC_TYPE=(
        ('MONT','Mensual'),
        # ('QUIN','Quincenal'),
        ('WEEK','Semanal'),
        ('DAY','Diario'),
        ('OT','OneTime'),
    )

    frecuency = models.CharField(choices=FREC_TYPE, max_length=50)
    metafreq = models.CharField(max_length=50, validators=[int_list_validator], blank=True, null=True)

    class Meta:
        verbose_name = "Asignment"
        verbose_name_plural = "Asignments"

    @property
    def days(self):

        begining = localdate() if self.last is None else self.last 
        meta =  None if self.metafreq is None else self.metafreq.split(',')

        if self.frecuency == 'DAY':
            if meta is None:
                return 1
            return int(meta[0])

        if self.frecuency == 'WEEK':
            actual_weekday = begining.weekday()
            weekdays = [int(c) for c in meta]
            weekdays.sort()
            # import pdb; pdb.set_trace()
            next_weekday = next((wd for wd in weekdays if wd >= actual_weekday), min(weekdays)) 

            next_weekday = next_weekday + 1
            actual_wd = actual_weekday + 1
            if next_weekday > actual_wd:
                return next_weekday - actual_wd
            else:
                return (7 - actual_wd) + next_weekday

        if self.frecuency == 'MONT':
            if meta is None:
                mes = begining.month + 1
                dia = begining.day
            else:
                monthdays = [int(c) for c in meta]
                monthdays.sort()
                # import pdb; pdb.set_trace()
                dia = next((wd for wd in monthdays if wd >= begining.day), min(monthdays))
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
            # import pdb; pdb.set_trace()
            nextdate = datetime(day=dia, month=mes, year=ano).date()

            return (nextdate-begining).days


    def generate_next_ocurrence(self):
        # import pdb; pdb.set_trace()
        if self.last is None:
            return localtime.date + timedelta(self.days)
        else:
            return self.last + timedelta(self.days)

    def generate_next_report(self, begin_date=None):
        begin = begin_date if begin_date is not None else self.last 
        report={
            'metric':self.metric,
            'company':self.company,
            'begin':begin,
            'end':self.next_ocurrence,
            'deadline':self.deadline_date,
        }
        rep = Report(**report)
        rep.save()
        return rep        
    
    @property
    def deadline_date(self):
        return self.next_ocurrence + timedelta( self.delivery_time )

    def __str__(self):
        return f'{self.metric} every {self.frecuency} days'

    def save(self, *args, **kwargs):
        if self.frecuency != "OT":
            self.next_ocurrence = self.generate_next_ocurrence()
        self.active_report = self.generate_next_report()
        return super().save(*args, **kwargs)