# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 10:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0003_cpu_mem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu_mem',
            name='Precpu',
        ),
    ]