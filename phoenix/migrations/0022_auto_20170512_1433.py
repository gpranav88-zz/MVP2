# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0021_trigger_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trigger',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]