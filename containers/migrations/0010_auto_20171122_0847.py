# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0009_cpu_mem_men'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu_mem',
            name='Cpu',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]