# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-23 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170422_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertytype',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city_experience',
            field=models.ManyToManyField(blank=True, related_name='city_experience', to='mygeo.City'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='financing_experience',
            field=models.ManyToManyField(blank=True, to='experience.FinancingExperience'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='property_type',
            field=models.ManyToManyField(blank=True, to='core.PropertyType'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='renovation_experience',
            field=models.ManyToManyField(blank=True, to='experience.RenovationExperience'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tax_experience',
            field=models.ManyToManyField(blank=True, to='experience.TaxExperience'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tenant_experience',
            field=models.ManyToManyField(blank=True, to='experience.TenantExperience'),
        ),
    ]