# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_info_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='Images_Size',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]