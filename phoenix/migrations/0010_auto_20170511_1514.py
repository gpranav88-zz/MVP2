# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0009_auto_20170511_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='services',
            field=models.CharField(default='identity', max_length=10),
        ),
    ]
