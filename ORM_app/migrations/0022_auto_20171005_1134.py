# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM_app', '0021_auto_20171004_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bamilo',
            old_name='classification',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='bamilo',
            old_name='classification_1',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='bamilo',
            old_name='classification_2',
            new_name='category1',
        ),
        migrations.RenameField(
            model_name='digikala',
            old_name='classification',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='digikala',
            old_name='item_name',
            new_name='brand_fa',
        ),
        migrations.RenameField(
            model_name='digikala',
            old_name='item_persian_name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='digikala',
            old_name='discount_price',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='digikalaids',
            old_name='classification',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='digikala',
            name='address',
        ),
        migrations.RemoveField(
            model_name='digikala',
            name='discount_percent',
        ),
        migrations.RemoveField(
            model_name='digikala',
            name='item_image',
        ),
        migrations.RemoveField(
            model_name='digikala',
            name='new_price',
        ),
        migrations.RemoveField(
            model_name='digikala',
            name='old_price',
        ),
        migrations.AddField(
            model_name='bamilo',
            name='category2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='bamilo',
            name='category3',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikala',
            name='category1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikala',
            name='category2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikala',
            name='category3',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='digikalaids',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]