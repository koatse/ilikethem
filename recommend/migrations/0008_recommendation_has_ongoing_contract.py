# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0007_auto_20170408_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='has_ongoing_contract',
            field=models.BooleanField(default=False),
        ),
    ]
