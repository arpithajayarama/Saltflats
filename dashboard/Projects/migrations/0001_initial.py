# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=30)),
                ('subject_major', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('hr_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('dateofjoin', models.DateField()),
                ('maxhrs_week', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('devlivary_date', models.DateField()),
                ('client_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=8)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.Client')),
                ('contractor', models.ManyToManyField(to='Projects.Contractor')),
            ],
        ),
    ]
