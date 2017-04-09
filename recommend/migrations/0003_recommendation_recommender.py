# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_userprofile_intro'),
        ('recommend', '0002_auto_20170408_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='recommender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile'),
        ),
    ]