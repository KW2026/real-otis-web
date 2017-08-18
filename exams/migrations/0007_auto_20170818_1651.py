# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20170810_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(blank=True, help_text='When the assignment is due. Leave blank if not active this semester.', null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='name',
            field=models.CharField(help_text='Name / description of the assignment', max_length=80, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='semester',
        ),
    ]
