# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-23 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20170423_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
