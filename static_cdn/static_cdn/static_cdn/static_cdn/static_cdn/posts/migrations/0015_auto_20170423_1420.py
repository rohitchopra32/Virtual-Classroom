# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-23 08:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20170423_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 23, 8, 50, 29, 590474, tzinfo=utc)),
        ),
    ]
