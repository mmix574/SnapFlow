# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('chinese_name', models.CharField(blank=True, max_length=20, null=True)),
                ('create_time', models.DateTimeField(auto_now=True, null=True)),
                ('last_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('create_user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('chinese_name', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('last_time', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Class')),
            ],
            options={
                'verbose_name': '帖子类型',
                'verbose_name_plural': '帖子类型',
            },
        ),
        migrations.CreateModel(
            name='TAG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(blank=True, max_length=20)),
                ('content', models.TextField(default='')),
                ('create_time', models.DateTimeField(auto_now=True, null=True)),
                ('last_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('create_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
