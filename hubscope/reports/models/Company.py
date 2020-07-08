import calendar 
from django.db import models
from datetime import  datetime, timedelta
from django.utils.timezone import localdate
from hubscope.accounts.models import User

from django.core.exceptions import ValidationError
from django.core.validators import int_list_validator
from functools import reduce


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