# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0011_auto_20160822_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='service_member',
            new_name='marine',
        ),
        migrations.RenameField(
            model_name='pledge',
            old_name='service_member',
            new_name='marine',
        ),
    ]
