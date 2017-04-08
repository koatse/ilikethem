# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_investmentexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentexperience',
            name='financing_experience',
            field=models.ManyToManyField(blank=True, to='core.FinancingExperience'),
        ),
        migrations.AlterField(
            model_name='investmentexperience',
            name='property_type',
            field=models.ManyToManyField(blank=True, to='core.PropertyType'),
        ),
        migrations.AlterField(
            model_name='investmentexperience',
            name='renovation_experience',
            field=models.ManyToManyField(blank=True, to='core.RenovationExperience'),
        ),
        migrations.AlterField(
            model_name='investmentexperience',
            name='tax_experience',
            field=models.ManyToManyField(blank=True, to='core.TaxExperience'),
        ),
        migrations.AlterField(
            model_name='investmentexperience',
            name='tenant_experience',
            field=models.ManyToManyField(blank=True, to='core.TenantExperience'),
        ),
    ]
