# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0003_recommendation_recommender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='recommender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile'),
        ),
    ]
