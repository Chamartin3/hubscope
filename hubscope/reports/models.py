from django.db import models
from datetime import  datetime
# Create your models here.

class Company(models.Model):
    '''
        Cada una de las empresas que esta 
        asociada a los rep
    '''
    name = models.CharField(blank=True, max_length=100)
    desc = models.TextField()
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companys"
    def __str__(self):
        return f'{self.name}'

class Asignment(models.Model):
    '''
        Conjunto de indicadores que deben reportarse
        Asocia empresa con indicadores y una periodicidad
    '''
    name = models.CharField(blank=True, max_length=100)
    company = models.ForeignKey(Company, 
        on_delete=models.CASCADE, 
        related_name='expected_report')
    last = models.DateField(blank=True)
    frecuency  = models.IntegerField(blank=True, default=1)

    class Meta:
        verbose_name = "Asignment"
        verbose_name_plural = "Asignments"
    def __str__(self):
        return f'{self.company.name}'

class Indicator(models.Model):
    '''
        Indicador Reportado   
    '''
    TIPOS = [
        ('C','Cuantitativo'),
        ('Q','Cualitativo')
    ]
    name = models.CharField(blank=True, max_length=100)
    tipo = models.CharField(choices=TIPOS, blank=True, max_length=100)
    class Meta:
        verbose_name = "Indicator"
        verbose_name_plural = "Indicators"
    def __str__(self):
        return f'{self.name} {self.tipo}'

class Report(models.Model):
    """Es el Registro de información cruda """
    asignment = models.ForeignKey(Asignment, 
        on_delete=models.CASCADE, 
        related_name='acomplishment'
    )
    indicator = models.ForeignKey(Indicator,
        on_delete=models.CASCADE, 
        related_name='responses'
    )

    # Traking Data 
    created_at = models.DateTimeField(auto_now_add=True)
    registered_by = models.ForeignKey('accounts.User',
        on_delete=models.CASCADE, 
        related_name='registros'
    )
    updated_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('accounts.User',
        on_delete=models.CASCADE, 
        related_name='modificados'
    )

    # Valor testual io numerico
    num_value = models.FloatField(blank=True, null=True)
    text_value = models.CharField(blank=True, null=True, max_length=50)
    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    @property
    def value(self):
        if self.indicator.tipo == 'C':
            return self.num_value
        return self.text_value

    def __str__(self):
        """Unicode representation of Response."""
        return f'{self.indicator}({self.created_at}): {self.value}'

class CompanyRole(models.Model):
    """Model definition for CompanyRole."""
    person = models.ForeignKey('accounts.User',
        on_delete=models.CASCADE, 
        related_name='role'
    )    
    company = models.ForeignKey(Company,
        on_delete=models.CASCADE, 
        related_name='member'
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        """Unicode representation of CompanyRole."""
        return f'{self.name} en {self.company.name}: {self.person.username}'