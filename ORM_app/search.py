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

from  documents import MasirDocument
def search(tag):
    from django.db.models import Q
    import re
    app = apps.get_app_config('ORM_app')
    a = []
    tag = tag.replace("+", " ")
    main_tag = tag
    from googletrans import Translator
    translator = Translator()
    translations = translator.translate(tag,src='fa',dest='en')
    print("1,",tag)
    tag = translations.text
    print("search tags = ",translations.text)
    print("2,", tag)
    if len(tag.split(" ")) == 1:
        if tag.upper() in [x.upper() for x in category_list]:
            print(tag)
            a = search_category(tag)
        else:
            a = search_product(main_tag)
    elif len(tag.split(" ")) == 2:
        a = two_word_search(main_tag)
    return a

def search_category(category):
    print("category = ", category)
    s = MasirDocument.search().filter("match",masir_cat=category).sort(
            {"_score" : {"order":"desc"}},
            {"discount_price" : {"order": "desc"}}
        )[:1000].to_queryset()
    for p in s:
        p.new_price = p.new_price/10
        p.old_price = p.old_price/10
        p.discount_price = p.discount_price/10
    return s
def search_product(category):
    print("searched text = ", category)
    s = MasirDocument.search().query("match",item_name=category)\
    .sort(
        # {"_score": {"order": "desc"}},
        {"discount_price": {"order": "desc"}}
    )[:1000].to_queryset()
    for p in s:
        p.new_price = p.new_price / 10
        p.old_price = p.old_price / 10
        p.discount_price = p.discount_price / 10
    return s

    # app = apps.get_app_config('ORM_app')
    # for model_name, model in app.models.items():
    #     if model.__name__ == "Masir":
    #         products = model.objects.filter(
    #             Q(masir_cat__icontains=category) |
    #             Q(item_name__icontains=category) |
    #             Q(brand__icontains=category)
    #                                         ).order_by('-discount_price')
    #         if len(products) != 0:
    #             a = products
    #             for p in products:
    #                 p.new_price = p.new_price/10
    #                 p.old_price = p.old_price/10
    #                 p.discount_price = p.discount_price/10
    # return a

def two_word_search(tag):
    print("two word searched text = ", tag)
    s = MasirDocument.search().query("match", item_name=tag) \
            .sort(
        # {"_score": {"order": "desc"}},
        {"discount_price": {"order": "desc"}}
    )[:1000].to_queryset()
    for p in s:
        p.new_price = p.new_price / 10
        p.old_price = p.old_price / 10
        p.discount_price = p.discount_price / 10
    return s
    # from fuzzywuzzy import fuzz
    # print("ttttag = ",tag,tag.split(" ")[0],tag.split(" ")[1])
    # app = apps.get_app_config('ORM_app')
    # a=[]
    # for model_name, model in app.models.items():
    #     if model.__name__ == "Masir":
    #         if tag.split(" ")[1].upper() in [x.upper() for x in category_list]:
    #             products = model.objects.filter(
    #                 Q(masir_cat__iexact=tag.split(" ")[1])).order_by('-discount_price')
    #             for p in products:
    #
    #                 similarity = fuzz.partial_ratio(tag, str(p.masir_cat))
    #                 print(similarity)
    #                 if similarity > 55:
    #                     p.new_price = p.new_price / 10
    #                     p.old_price = p.old_price / 10
    #                     p.discount_price = p.discount_price / 10
    #                     a.append(p)
    # return a