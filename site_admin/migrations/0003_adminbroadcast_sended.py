# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0002_auto_20170416_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminbroadcast',
            name='sended',
            field=models.BooleanField(default=0),
        ),
    ]
