# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Amount Donated')),
                ('message', models.TextField(max_length=500)),
                ('public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Marine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount_raised', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Amount Raised')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.URLField()),
                ('site', models.URLField()),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraising.Donor'),
        ),
        migrations.AddField(
            model_name='donation',
            name='marine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraising.Marine'),
        ),
    ]
