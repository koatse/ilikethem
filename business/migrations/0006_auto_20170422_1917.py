# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-22 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_businessprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='city_headquarter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygeo.City', verbose_name='City of main office'),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Business email'),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Your name or your company name'),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Business phone'),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='service',
            field=models.ManyToManyField(to='business.BusinessService', verbose_name='Business services provided: (multi-select)'),
        ),
    ]
