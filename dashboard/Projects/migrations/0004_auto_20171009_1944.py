# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_auto_20171009_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=50, verbose_name='ADDRESS'),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=60, verbose_name='CITY'),
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(max_length=50, verbose_name='COMPANY'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='FIRST NAME'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='LAST NAME'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=50, verbose_name='PHONE NUMBER'),
        ),
        migrations.AlterField(
            model_name='client',
            name='state_province',
            field=models.CharField(max_length=30, verbose_name='STATE'),
        ),
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=38, verbose_name='BUDGET PER MONTH'),
        ),
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.Client', verbose_name='CLIENT'),
        ),
        migrations.AlterField(
            model_name='project',
            name='client_cost',
            field=models.DecimalField(decimal_places=2, max_digits=16, verbose_name='RATE PER HOUR'),
        ),
        migrations.AlterField(
            model_name='project',
            name='contractor',
            field=models.ManyToManyField(to='Projects.Contractor', verbose_name='CONTRACTOR'),
        ),
        migrations.AlterField(
            model_name='project',
            name='devlivary_date',
            field=models.DateField(verbose_name='END DATE'),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectname',
            field=models.CharField(max_length=100, verbose_name='PROJECT NAME'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name='START DATE'),
        ),
    ]