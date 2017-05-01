# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-01 20:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fourms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to=student.models.download_location)),
                ('first_name', models.CharField(max_length=120, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('roll_no', models.CharField(max_length=20, unique=True)),
                ('batch', models.IntegerField(choices=[(2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017')], default=None, null=True)),
                ('branch', models.CharField(choices=[('', 'branch'), ('cse', 'CSE'), ('ece', 'ECE'), ('mae', 'MAE')], default=None, max_length=3, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('contact', models.BigIntegerField(null=True)),
                ('address', models.TextField(max_length=300, null=True)),
                ('first', models.BooleanField(default=True)),
                ('classroom', models.ManyToManyField(related_name='students', to='classroom.Classroom')),
                ('fourms', models.ManyToManyField(related_name='studentforum', to='fourms.Fourms')),
                ('username', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
