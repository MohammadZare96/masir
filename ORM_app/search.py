# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from django.apps import apps
from django.db.models import Q
from models import *


category_list = [
    'Bed_Bath',
    'Bicycle',
    'Camera',
    'Car_Equipment',
    'Carpet',
    'Clean',
    'Computer_Parts',
    'Decorative',
    'Digital_Accessories',
    'Electrical_Personal',
    'Electrical_Tool',
    'Film_Music',
    'Game_Console',
    'General_Home',
    'Handcraft',
    'Hand_Tool',
    'Health',
    'Home_Electrical_Appliance',
    'Home_kitchen_Appliances',
    'Jewelery',
    'Kid',
    'Laptop',
    'Makeup',
    'Men_Accessories',
    'Men_Shoes',
    'Men_Sport_Clothes',
    'Men_Women_Accessories',
    'Mobile',
    'Music_Tool',
    'Office_Machines',
    'Perfume',
    'Publication',
    'Software_Game',
    'Sport_Shoes',
    'Sport_tools',
    'Sport_Tools',
    'Stationery',
    'Tablet',
    'Toy',
    'Training',
    'Traveling_Equipment',
    'Watch',
    'Women_Shoes',
    'Women_Sport_Clothes'
]


def filter(
        min_discount_price,
        max_discount_price,
        min_discount_percent,
        max_discount_percent,
        min_price,
        max_price,
        websites,
        brands,
        masir_cat
        ):
    app = apps.get_app_config('ORM_app')
    a = []
    for model_name, model in app.models.items():
        if "Product" in model.__name__:
            for site in websites:
                if site in model.__name__:
                    for brand in brands:
                        for cat in masir_cat:
                            a.append(list(set(model.objects.filter(
                                discount_price__lte=max_discount_price,
                                discount_price__gte=min_discount_price,
                                discount_percent__lte=max_discount_percent,
                                discount_percent__gte=min_discount_percent,
                                new_price__lte=max_price,
                                new_price__gte=min_price,
                                brand=brand,
                                masir_cat=cat
                            ).order_by("-discount_price"))))
    return a

def search(tag):
    from django.db.models import Q
    import re
    app = apps.get_app_config('ORM_app')
    a = []
    from googletrans import Translator
    translator = Translator()
    translations = translator.translate(tag,src='fa',dest='en')
    print("1,",tag)
    tag = translations.text
    print("search tags = ",translations.text)
    print("2,", tag)
    if len(tag.split("%20")) == 1:
        if tag.upper() in [x.upper() for x in category_list]:
            print(tag)
            a = search_category(tag)
        else:
            a = search_product(tag)

            # else:
            #     products = model.objects.filter(
            #         Q(item_name__icontains)
            #     )
            # counter = [0]*len(products)
            # for i in range(0,len(products)):
            #     for item in tag:
            #         if re.search(item, products[i].masir_cat, re.IGNORECASE):
            #             counter[i]+=1
            #         elif re.search(item, products[i].item_name, re.IGNORECASE):
            #             counter[i]+=1
            #         elif re.search(item, products[i].brand, re.IGNORECASE):
            #             counter[i]+=1
            # print ("max=",max(counter))
            # for j in range(10, -1, -1):
            #     for i in range(0, len(counter)):
            #         if counter[i] == j and j != 0:
            #             a.append(products[i])
            # b.append(a)
            # print(counter[42301])
            # order_by("-discount_price")
            # a.append(list(set(products[:10])))
            # print(a)
    # print("Produts with 4 match",a)
    # print(b[0][0].item_name)
    # print(b[0][0].masir_cat)
    return a

def search_category(category):
    print("category = ", category)
    app = apps.get_app_config('ORM_app')
    for model_name, model in app.models.items():
        if model.__name__ == "Masir":
            products = model.objects.filter(masir_cat__iexact=category).order_by('-discount_price')
            if len(products) != 0:
                a = products
                for p in products:
                    p.new_price = p.new_price/10
                    p.old_price = p.old_price/10
                    p.discount_price = p.discount_price/10
    return a
def search_product(category):
    print("category = ", category)
    app = apps.get_app_config('ORM_app')
    for model_name, model in app.models.items():
        if model.__name__ == "Masir":
            products = model.objects.filter(
                Q(masir_cat__icontains=category) |
                Q(item_name__icontains=category) |
                Q(brand__icontains=category)
                                            ).order_by('-discount_price')
            if len(products) != 0:
                a = products
                for p in products:
                    p.new_price = p.new_price/10
                    p.old_price = p.old_price/10
                    p.discount_price = p.discount_price/10
    return a