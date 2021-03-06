# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_auto_20170412_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='self_introduction',
            field=models.CharField(blank=True, max_length=300, verbose_name='自我介绍'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='work_nickname',
            field=models.CharField(blank=True, max_length=20, verbose_name='职位'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='work_place',
            field=models.CharField(blank=True, max_length=20, verbose_name='工作单位'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='work_year',
            field=models.IntegerField(blank=True, default=0, verbose_name='工作年限'),
        ),
    ]
