# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0020_auto_20170413_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='set_avatar',
        ),
    ]
