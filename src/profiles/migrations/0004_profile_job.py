# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-06-05 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(default=True, max_length=120),
        ),
    ]
