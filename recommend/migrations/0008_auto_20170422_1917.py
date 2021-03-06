# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-22 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0007_recommendation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='city_serviced',
            field=models.ManyToManyField(to='mygeo.City', verbose_name='City where they provided service to me'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='is_repeated_customer',
            field=models.BooleanField(default=False, verbose_name='I am a repeated customer of this business'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='main_reason_to_reuse',
            field=models.IntegerField(choices=[(0, 'LowPrice'), (1, 'Expertise'), (2, 'CustomerService'), (3, 'Availability'), (4, 'Workmanship'), (5, 'Satisfied')], default=5, verbose_name='Why I like them:'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Business Owner/Company name'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='on_active_contract',
            field=models.BooleanField(default=False, verbose_name='I have a ongoing contract with this business'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='pricing',
            field=models.IntegerField(choices=[(0, 'Budget'), (1, 'AveragePrice'), (2, 'Premium')], default=1, verbose_name='Price point'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='satisfaction',
            field=models.IntegerField(choices=[(0, 'GOOD'), (1, 'GREAT'), (2, 'AWESOME'), (3, 'PERFECT')], default=0, verbose_name='They make me feel'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='total_money_spent',
            field=models.IntegerField(choices=[(-1, 'Not Applicable'), (0, '$0 - $99'), (1, '$100 - $199'), (2, '$200 - $499'), (3, '$500 - $999'), (4, '$1,000 - $1,999'), (5, '$2,000 - $4,999'), (6, '$5,000 - $9,999'), (7, '$10,000 - $19,999'), (8, '$20,000 - $49,999'), (9, '$50,000 - $99,999'), (10, '$100,000 - $199,999'), (11, '$200,000 - $499,999'), (12, '$500,000 - $999,999')], default=0, verbose_name='Total purchase so far'),
        ),
    ]
