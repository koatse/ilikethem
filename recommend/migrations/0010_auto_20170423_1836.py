# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-23 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0009_auto_20170422_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='city_serviced',
            field=models.ManyToManyField(to='mygeo.City', verbose_name='Cities where they provided service to me'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='story',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='My happy story working with them:'),
        ),
    ]
