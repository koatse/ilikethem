# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0005_auto_20170408_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='pricing',
            field=models.IntegerField(choices=[(0, 'Budget'), (1, 'Average'), (2, 'Premium')], default=1),
        ),
    ]