# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-15 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='default location', max_length=120),
        ),
    ]
