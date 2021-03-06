# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-07 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotSystem', '0003_auto_20180426_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='name',
        ),
        migrations.RemoveField(
            model_name='data',
            name='value',
        ),
        migrations.AddField(
            model_name='data',
            name='at',
            field=models.CharField(default='', max_length=20, verbose_name='\u5927\u6c14\u538b'),
        ),
        migrations.AddField(
            model_name='data',
            name='ch4',
            field=models.CharField(default='', max_length=20, verbose_name='CH4'),
        ),
        migrations.AddField(
            model_name='data',
            name='humi',
            field=models.CharField(default='', max_length=20, verbose_name='\u6e7f\u5ea6'),
        ),
        migrations.AddField(
            model_name='data',
            name='temp',
            field=models.CharField(default='', max_length=20, verbose_name='\u6e29\u5ea6'),
        ),
    ]
