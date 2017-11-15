# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import *


# class TorobAdmin(admin.ModelAdmin):
#     def item_name(obj):
#         return '<a href="%s">%s</a>' % (obj.address, obj.item_name)
#     item_name.allow_tags = True
#     item_name.short_description = 'Item Name'
#     list_display = ('id', item_name, 'new_price', 'old_price', 'discount_price', 'discount_percent')
#     search_fields = ['id', 'item_name', 'new_price', 'old_price', 'discount_price','discount_percent']
#     # list_filter = ['item_name']
class MasirAdmin(admin.ModelAdmin):
    def item_name(obj):
        return '<a href="%s">%s</a>' % (obj.address, obj.item_name)
    def item_image(obj):
        return '<a href="%s">%s</a>' % (obj.item_image, "image")

    item_name.allow_tags = True
    item_name.short_description = 'Item Name'
    item_image.allow_tags = True
    item_image.short_description = 'Image'
    list_display = (
        # 'time',
        'id',
        item_name,
        # 'new_price',
        # 'old_price',
        # 'discount_price',
        # 'discount_percent',
        item_image,
        'brand',
        'masir_cat',
    )
    list_filter = ['masir_cat']



class BamiloAdmin(admin.ModelAdmin):
    def item_name(obj):
        return '<a href="%s">%s</a>' % (obj.address, obj.item_name)
    def item_image(obj):
        return '<a href="%s">%s</a>' % (obj.item_image, "image")
    item_name.allow_tags = True
    item_name.short_description = 'Item Name'
    item_image.allow_tags = True
    item_image.short_description = 'Image'
    list_display = (
        # 'time',
        'id',
        item_name,
        # 'new_price',
        # 'old_price',
        # 'discount_price',
        # 'discount_percent',
        # item_image,
        # 'brand',
        'masir_cat',
        # 'categoryfa',
        # 'categoryfa1',
        # 'categoryfa2',
        # 'categoryfa3',
        # 'categoryfa4',
        'category1',
        'category2',
        'category3'
    )
    search_fields = [
        'id',
        'item_name',
        'new_price',
        'old_price',
        'discount_price',
        'discount_percent',
        # 'masir_cat',
        # 'brand',
        'category1',
        'category2',
        'category3'
    ]
    list_filter = [
        # 'brand',
        'masir_cat',
        # 'categoryfa',
        # 'categoryfa1',
        # 'categoryfa2',
        # 'categoryfa3',
        # 'categoryfa4',
        'category1',
        'category2',
        # 'category3',
        # 'category4',
        # 'category5'
    ]
class BamiloUrlsL2Admin(admin.ModelAdmin):
    def url(obj):
        return '<a href="%s">%s</a>' % (obj.url, obj.url)
    url.allow_tags = True
    url.short_description = 'URL'
    list_display = [url, 'category1', 'category2']
    list_filter = ['category1', 'category2']
    search_fields = ['url']
class BamiloIdsAdmin(admin.ModelAdmin):
    def url(obj):
        return '<a href="%s">%s</a>' % (obj.url, obj.url)
    url.allow_tags = True
    url.short_description = 'URL'
    list_display = ["id",url, 'category1','category2']
    search_fields = ['url','category1','category2']
    list_filter = [
        'category1',
        'category2'
    ]




class DigikalaAdmin(admin.ModelAdmin):

    def name(obj):
        return Product_Digikala.objects.filter(product_id=obj.product_id)[0].item_name
    def pname(obj):
        return Product_Digikala.objects.filter(product_id=obj.product_id)[0].item_persian_name
    def categoryen(obj):
        return Product_Digikala.objects.filter(product_id=obj.product_id)[0].category
    def newprice(obj):
        return Product_Digikala.objects.filter(product_id=obj.product_id)[0].new_price
    def discountprice(obj):
        return Product_Digikala.objects.filter(product_id=obj.product_id)[0].discount_price
    def discount(obj):
        return Product_Digikala.objects.filter(product_id=obj.product_id)[0].discount_percent
    list_display = (
        'time',
        name,
        pname,
        categoryen,
        'id',
        'product_id',
        'brand_fa',
        newprice,
        discountprice,
        discount,
        'brand',
        'masir_cat',
        'category',
        'category1',
        'category2'
    )
    search_fields = ['brand_fa', 'brand', 'category', 'category1', 'category2','product_id']
    list_filter = ['masir_cat']


class ProductDigikalaAdmin(admin.ModelAdmin):
    def item_persian_name(obj):
        return '<a href="%s">%s</a>' % (obj.address, obj.item_persian_name)
    def item_image(obj):
        return '<a href="%s">%s</a>' % (obj.item_image, "image")
    item_persian_name.allow_tags = True
    item_image.allow_tags = True

    item_image.short_description = 'Item Name'
    item_persian_name.short_description = 'Item Name'
    list_display = (
        'time',
        item_persian_name,
        'item_name',
        'brand',
        'masir_cat',
        'category1',
        'category2',
        # 'new_price',
        # 'old_price',
        'discount_price',
        # 'discount_percent',
        # item_image,
        "product_id"
    )
    search_fields = ['product_id', 'item_persian_name', 'item_name', 'address']
    list_filter = [
        'masir_cat',
        'category1',
        'category2'
    ]
class DigikalaUrlsL2Admin(admin.ModelAdmin):
    def url(obj):
        return '<a href="%s">%s</a>' % (obj.url, obj.url)
    url.allow_tags = True
    url.short_description = 'URL'
    list_display = [url, 'category1', 'category2']
    list_filter = ['category1', 'category2']
    search_fields = ['url']

class UrlAdmin(admin.ModelAdmin):
    def url(obj):
        return '<a href="%s">%s</a>' % (obj.url, obj.url)
    url.allow_tags = True
    url.short_description = 'URL'
    list_display = ['time','id',url, "flag"]
    search_fields = ['url']

class DigikalaUrlAdmin(admin.ModelAdmin):
    def url(obj):
        return '<a href="%s">%s</a>' % (obj.url, obj.url)
    url.allow_tags = True
    url.short_description = 'URL'
    list_display = ['time','id',url]
    search_fields = ['url']
class CategoryAdmin(admin.ModelAdmin):
    def category(obj):
        return '<a href="%s">%s</a>' % (obj.category, obj.category)
    category.allow_tags = True
    list_display = [category]


# admin.site.register(Torob, TorobAdmin)
admin.site.register(Product_Bamilo, BamiloAdmin)
admin.site.register(Digikala_details, DigikalaAdmin)
admin.site.register(Masir, MasirAdmin)
admin.site.register(DigikalaUrls, DigikalaUrlAdmin)
admin.site.register(Product_Digikala, ProductDigikalaAdmin)
admin.site.register(BamiloIds, BamiloIdsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BamiloUrlsL2, BamiloUrlsL2Admin)
admin.site.register(DigikalaUrlsL2, DigikalaUrlsL2Admin)
# admin.site.register(TorobIds, UrlAdmin)