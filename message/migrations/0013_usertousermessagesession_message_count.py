# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0012_remove_usertousermessage_is_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertousermessagesession',
            name='message_count',
            field=models.IntegerField(default=0),
        ),
    ]
