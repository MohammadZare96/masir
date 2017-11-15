# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import timezone

from datetime import datetime
import django
from django.db import models

# Create your models here.

class Masir(models.Model):
    item_name = models.TextField(default='')
    new_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    old_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    discount_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    discount_percent = models.FloatField()
    address = models.URLField(max_length=1000)
    item_image = models.URLField(max_length=1000, default='')
    masir_cat = models.TextField(default='Other')
    brand = models.TextField(default='')
    time = models.DateTimeField(default=django.utils.timezone.now)




class Torob(models.Model):
    # id = models.DecimalField(primary_key=True)
    item_name = models.TextField(default='')
    new_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    old_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    discount_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    discount_percent = models.FloatField()
    address = models.URLField(max_length=1000)
    time = models.DateTimeField(default=django.utils.timezone.now)




class Product_Bamilo(models.Model):
    # id = models.DecimalField(primary_key=True)
    item_name = models.TextField(default='')
    new_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    old_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    discount_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    discount_percent = models.FloatField()
    address = models.URLField(max_length=1000)
    item_image = models.URLField(max_length=1000, default='')
    masir_cat = models.TextField(default='')
    categoryfa = models.TextField(default='')
    categoryfa1 = models.TextField(default='')
    categoryfa2 = models.TextField(default='')
    categoryfa3 = models.TextField(default='')
    categoryfa4 = models.TextField(default='')

    category1 = models.TextField(default='')
    category2 = models.TextField(default='')
    category3 = models.TextField(default='')
    category4 = models.TextField(default='')
    category5 = models.TextField(default='')
    brand = models.TextField(default='')
    time = models.DateTimeField(default=django.utils.timezone.now)
    # detail_classification = models.TextField()

class BamiloUrlsL1(models.Model):
    url = models.TextField(default='')
    category1 = models.TextField(default='')

class BamiloUrlsL2(models.Model):
    url = models.TextField(default='')
    category1 = models.TextField(default='')
    category2 = models.TextField(default='')






class Digikala_details(models.Model):
    # id = models.DecimalField(primary_key=True)
    # item_persian_name = models.TextField(default='')
    # item_name = models.TextField(default='')
    # new_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    # old_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    # discount_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    # discount_percent = models.FloatField()
    # address = models.URLField(max_length=1000)
    # item_image = models.URLField(max_length=1000, default='')
    # classification = models.TextField(default='')
    product_id = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    brand_fa = models.TextField(default='')
    brand = models.TextField(default='')
    masir_cat = models.TextField(default='')
    category = models.TextField(default='')
    category1 = models.TextField(default='')
    category2 = models.TextField(default='')
    category3 = models.TextField(default='')
    time = models.DateTimeField(default=django.utils.timezone.now)


class DigikalaUrls(models.Model):
    url = models.TextField(default='')
    time = models.DateTimeField(default=django.utils.timezone.now)
class DigikalaUrlsL1(models.Model):
    url = models.TextField(default='')
    category1 = models.TextField(default='')

class DigikalaUrlsL2(models.Model):
    url = models.TextField(default='')
    category1 = models.TextField(default='')
    category2 = models.TextField(default='')

class Product_Digikala(models.Model):
    item_persian_name = models.TextField(default='')
    item_name = models.TextField(default='')
    new_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    old_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    discount_price = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    discount_percent = models.FloatField(default=0)
    address = models.URLField(max_length=1000)
    item_image = models.URLField(max_length=1000, default='')
    product_id = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    category1 = models.TextField(default='')
    category2 = models.TextField(default='')
    masir_cat = models.TextField(default='')
    brand = models.TextField(default='')
    brand_fa = models.TextField(default='')
    time = models.DateTimeField(default=django.utils.timezone.now)

class BamiloIds(models.Model):
    url = models.URLField(max_length=1000)
    time = models.DateTimeField(default=django.utils.timezone.now)
    flag = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)
    category1 = models.TextField(default='')
    category2 = models.TextField(default='')

class TorobIds(models.Model):
    url = models.URLField(max_length=1000)
    time = models.DateTimeField(default=django.utils.timezone.now)



class TorobShopId(models.Model):
    shopid = models.IntegerField()
    time = models.DateTimeField(default=django.utils.timezone.now)

class Category(models.Model):
    category = models.TextField(default='')
    pid = models.DecimalField(max_digits=1000, decimal_places=0, blank=True, null=True, default=0)