# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-28 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
