# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0024_auto_20171005_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(default='')),
            ],
        ),
    ]
