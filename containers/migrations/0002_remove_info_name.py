# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 02:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='Name',
        ),
    ]
