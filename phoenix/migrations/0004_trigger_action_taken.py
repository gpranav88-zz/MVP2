# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0003_auto_20170511_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='action_taken',
            field=models.CharField(default='None', max_length=50),
        ),
    ]