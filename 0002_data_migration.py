# Generated by Django 2.2.8 on 2020-06-10 23:19

from django.db import migrations
import json

def getCompanies():
    with open('data/Companies.json','r') as file:
        return json.loads(file.read())
        
def getIndicadores():
    with open('data/Indicadores.json','r') as file:
        return json.loads(file.read())

def setMetric(Model,metric):
    modelname=metric.pop('name')
    instance, created = Model.objects.get_or_create(
        name = modelname,
        defaults=metric
        )
    return Model.objects.get(pk=instance.id)

def migrate(apps, schema_editor):
    Company = apps.get_model('reports','Company')
    company_instances = [Company(**c) for c in getCompanies()]
    Company.objects.bulk_create(company_instances)

    # import pdb; pdb.set_trace()
    Metric = apps.get_model('reports','Metric')
    Indicator = apps.get_model('reports','Indicator')
    Goal = apps.get_model('reports','Goal')

    for ind in getIndicadores():
        metrics = ind.pop('metrics')
        periods = ind.pop('periods')
        indi_instance = Indicator.objects.create(**ind)
        indi_instance.metrics.set([setMetric(Metric,m) for m in metrics])
        for p in periods:
            p['indicator'] = indi_instance
            Goal.create(**p)

def revert(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, revert)
    ]
