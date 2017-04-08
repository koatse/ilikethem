# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygeo', '0001_initial'),
        ('business', '0002_businessprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='city_headquarter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygeo.City'),
        ),
    ]