# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170408_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygeo.City'),
        ),
    ]
