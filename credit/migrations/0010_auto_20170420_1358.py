# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0009_auto_20170420_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='everydaycreditlog',
            name='user',
        ),
        migrations.AddField(
            model_name='onlinelog',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EveryDayCreditLog',
        ),
    ]
