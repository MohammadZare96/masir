# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 13:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0020_auto_20171004_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bamiloids',
            old_name='last_flag',
            new_name='flag',
        ),
    ]