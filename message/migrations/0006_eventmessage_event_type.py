# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20170419_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmessage',
            name='event_type',
            field=models.CharField(choices=[('being_liked', '收到赞'), ('being_answering', '收到答案')], default='', max_length=20),
            preserve_default=False,
        ),
    ]
