# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='user',
        ),
        migrations.DeleteModel(
            name='Subjects',
        ),
    ]
