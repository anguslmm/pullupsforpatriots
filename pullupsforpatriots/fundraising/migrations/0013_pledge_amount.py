# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0012_auto_20160826_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
