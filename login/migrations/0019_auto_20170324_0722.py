# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_auto_20170324_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject3',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject4',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject5',
            field=models.CharField(default='', max_length=500),
        ),
    ]
