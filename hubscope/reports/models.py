from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(blank=True, max_length=100)
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companys"
    def __str__(self):
        pass

class Report(models.Model):
    company = models.ForeignKey('APP.OTHERMODEL', on_delete=models.CASCADE, related_name='', verbose_name='')
    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"
    def __str__(self):
        pass


class Indicator(models.Model):
    name = models.CharField(blank=True, max_length=100)
    type = models.CharField(blank=True, max_length=100)
    company = models.ForeignKey('APP.OTHERMODEL', on_delete=models.CASCADE, related_name='', verbose_name='')
    class Meta:
        verbose_name = "Indicator"
        verbose_name_plural = "Indicators"
    def __str__(self):
        pass
