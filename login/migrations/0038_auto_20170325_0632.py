# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0037_auto_20170325_0326'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubjectD',
            new_name='LightRoom',
        ),
        migrations.RenameModel(
            old_name='SubjectB',
            new_name='PhotoshopBasics',
        ),
        migrations.RenameModel(
            old_name='SubjectA',
            new_name='PhotoTutorials',
        ),
        migrations.RenameModel(
            old_name='SubjectC',
            new_name='SpecialEffects',
        ),
        migrations.RenameModel(
            old_name='SubjectE',
            new_name='TextEffects',
        ),
        migrations.DeleteModel(
            name='Suggestions',
        ),
    ]
