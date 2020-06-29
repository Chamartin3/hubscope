# Generated by Django 2.2.8 on 2020-06-10 23:19


from django.db import migrations
import csv

def getReports():
    with open('data/mockdata.csv','r') as file:
        return [ d for d in csv.DictReader(file) ]

def migrate(apps, schema_editor):
    Report = apps.get_model('reports','Report')
    Metric = apps.get_model('reports','Metric')
    metrics={}

    for rep in getReports():
        name=rep.pop('metric__name')
        if name not in metrics.keys():
            try:
                metrics[name]=Metric.objects.get(name=name)
            except Exception as e:
                print(name)
                print(e)
                import pdb; pdb.set_trace()              
        rep['metric'] =  metrics[name]
        Report.objects.create(**rep)

def revert(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_data_migration'),
    ]

    operations = [
        migrations.RunPython(migrate, revert)
    ]
