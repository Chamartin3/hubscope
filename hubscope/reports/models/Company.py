
from django.db import models

from hubscope.accounts.models import User

from functools import reduce
from itertools import chain


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


    @property
    def open_goals(self):
        goalsqs= [i.active_goals for i in self.indicators.all()]
        goals = []
        if len(goalsqs)>0:
            goals = list(chain(*goalsqs))
        return goals


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