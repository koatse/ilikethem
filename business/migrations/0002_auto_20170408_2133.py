# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='service',
            field=models.ManyToManyField(to='business.BusinessService'),
        ),
    ]
