# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmodel',
            name='result',
            field=models.IntegerField(null=True),
        ),
    ]