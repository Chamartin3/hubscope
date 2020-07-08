# Generated by Django 2.2.8 on 2020-06-10 23:19

from django.db import migrations
import json

def getReports():
    with open('data/Reports.json','r') as file:
        return json.loads(file.read())

def migrate(apps, schema_editor):
    Report = apps.get_model('reports','Report')
    Metric = apps.get_model('reports','Metric')

    for rep in getReports():
        name = rep.pop('metric__name')
        try:
            metric = Metric.objects.get(name=name)
        except Exception as e:
            print(name)
            print(e)
            import pdb; pdb.set_trace()
        rep['metric'] = metric
        Report.objects.create(**rep)

def revert(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_data_migration'),
    ]

    operations = [
        migrations.RunPython(migrate, revert)
    ]
