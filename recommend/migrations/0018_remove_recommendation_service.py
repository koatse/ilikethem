# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 19:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0017_auto_20170408_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='service',
        ),
    ]
