# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-04 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_student_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
    ]
