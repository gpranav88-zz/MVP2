# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0011_auto_20170511_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='attributes',
            field=models.CharField(choices=[('email', 'User Email'), ('cancelled_order', 'Cancelled Orders'), ('refund_order', 'Refund Orders')], default='email', max_length=10),
        ),
        migrations.AlterField(
            model_name='rule',
            name='services',
            field=models.CharField(choices=[('identity', 'IDENTITY'), ('order', 'ORDER')], default='identity', max_length=10),
        ),
    ]