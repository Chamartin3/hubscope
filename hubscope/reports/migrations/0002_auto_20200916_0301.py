# Generated by Django 2.2.8 on 2020-09-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignment',
            name='genetated_reports',
            field=models.ManyToManyField(related_name='asignment', to='reports.Report'),
        ),
    ]
