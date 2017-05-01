# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_student_first'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to=student.models.download_location),
        ),
    ]
