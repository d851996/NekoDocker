# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20171018_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Architecture',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='Containers',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='ContainersPaused',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='ContainersRunning',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='ContainersStopped',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='Images',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='MemTotal',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='NCPU',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='Name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='ServerVersion',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='ip',
            name='Ip',
            field=models.CharField(max_length=28),
        ),
    ]
