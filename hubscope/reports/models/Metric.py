import calendar 
from django.db import models
from datetime import  datetime, timedelta
from django.utils.timezone import localdate
from hubscope.accounts.models import User


from django.core.exceptions import ValidationError
from django.core.validators import int_list_validator
from functools import reduce

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
        # import pdb; pdb.set_trace()
        for k,v in kwargs.items():
            if k == 'begin':
                query['begin__gte'] = v
            elif k == 'end':
                query['end__lte'] = v
            else:
                query[k] = v

        return self.responses.filter(**query)