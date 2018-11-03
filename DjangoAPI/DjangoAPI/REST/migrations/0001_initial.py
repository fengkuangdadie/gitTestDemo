# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-01 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=32, unique=True)),
                ('d_legs', models.IntegerField(default=4)),
            ],
        ),
    ]
