# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 23:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_auto_20170324_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='subject1',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject2',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject3',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject4',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject5',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='subject',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
