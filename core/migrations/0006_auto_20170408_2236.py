# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygeo', '0001_initial'),
        ('core', '0005_userprofile_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='businessprofile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygeo.City'),
        ),
    ]
