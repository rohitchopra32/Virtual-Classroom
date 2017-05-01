# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=512)),
                ('roll_no', models.BigIntegerField()),
                ('batch', models.IntegerField(choices=[(2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016')], default=None)),
                ('branch', models.CharField(choices=[('', 'branch'), ('cse', 'CSE'), ('ece', 'ECE'), ('mae', 'MAE')], default=None, max_length=3)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('contact', models.BigIntegerField()),
                ('address', models.TextField(max_length=300)),
            ],
        ),
    ]
