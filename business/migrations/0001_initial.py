# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mygeo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('website', models.URLField(blank=True)),
                ('city_headquarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygeo.City')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='service',
            field=models.ManyToManyField(blank=True, to='business.BusinessService'),
        ),
    ]
