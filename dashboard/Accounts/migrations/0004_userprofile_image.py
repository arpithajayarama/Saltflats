# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20171110_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'profile_image'),
        ),
    ]