# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0017_auto_20170511_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trigger',
            name='signal_id',
        ),
        migrations.DeleteModel(
            name='Signal',
        ),
    ]