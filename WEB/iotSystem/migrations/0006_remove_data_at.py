# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-10 23:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iotSystem', '0005_auto_20180510_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='at',
        ),
    ]
