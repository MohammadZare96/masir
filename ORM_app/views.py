# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import itertools
import urllib

from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ORM_app.search import filter, search
from models import *

# # Create your views here.
# from ORM_app.filter import filter


def redirect_search(request):
    if request.method == 'POST':
        search_tag = request.POST.getlist('search')[0]
        print search_tag
        search_tag.replace(' ', "%20")
        return redirect('/'+search_tag)



def filtering(request):
    min_price = int(request.POST.get("amount").split(' ')[2].replace(',',''))*10
    max_price = int(request.POST.get("amount_1").split(' ')[2].replace(',',''))*10
    min_discount_price = int(request.POST.get("amount2").split(' ')[2].replace(',',''))*10
    max_discount_price = int(request.POST.get("amount2_1").split(' ')[2].replace(',',''))*10
    min_discount_percent = int(request.POST.get("amount3").split(' ')[2].replace(',',''))
    max_discount_percent = int(request.POST.get("amount3_1").split(' ')[2].replace(',',''))
    websites = request.POST.getlist("websites")
    brands = request.POST.getlist("brands")

    print(websites)
    print(brands)
    print(min_discount_price,
    max_discount_price,
    min_discount_percent,
    max_discount_percent,
    min_price,
    max_price)






def home(request):
    a = search("Mobile")
    return render(request, 'home.html', {
        "Slide_Products":a[10:13],
        "DayProducts":a[13:25]
    }
                  )

def general(request):
    url = request.build_absolute_uri()
    url = urllib.unquote(url).decode("utf-8")
    tag = url.split("/")[3]
    search_and_page = url.split("/")[4]
    if "page" in search_and_page and "search" in search_and_page:
        page_number = (search_and_page.split("&page=")[-1])
        print "page = ",page_number
        tag = (search_and_page.split("search="))[1].split("&page=")[0]
    elif "page" in search_and_page and "search" not in search_and_page:
        page_number = search_and_page[6:]
    elif "page" not in search_and_page and "search" in search_and_page:
        tag = url.split("/")[4].split("search=")[-1]
    item_per_page = 32
    product_list = search(tag)
    product_list_length = len(product_list)
    pages = product_list_length / item_per_page
    try:
        page_number = int(page_number)
    except:
        page_number = 1

    brands=[]
    for p in product_list:
        if p.brand not in brands:
            brands.append(p.brand)

    paginator = Paginator(product_list, 32)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj  = paginator.page(1)
    except EmptyPage:
        page_obj  = paginator.page(paginator.num_pages)
    if page_number * item_per_page < ((product_list_length)/item_per_page+1)* item_per_page +1:
        return render(request, 'shop.html', {
            "Products":product_list[item_per_page*(page_number-1):item_per_page*page_number],
            "websites":["digikala", "bamilo"],
            "brands":set(brands),
            "page_number":page_number,
            "pages":range(pages),
            "page_obj":page_obj
        }
                      )
    else:
        return HttpResponse("NOT FOUND")


def shop(request):
    a = filter(0,
               10000000000,
               0,
               100,
               0,
               10000000000,
               ['Bamilo'],
               ['Goldooneh', 'Samsung', 'Adidas'],
               ['Mobile', 'Men-Clothes', 'Hand-Tool']
               )
    print a
    a = list(itertools.chain.from_iterable(a))
    a.sort(key=lambda x: x.discount_price, reverse=True)
    return render(request, 'shop.html', {"Products":a[:9], "websites":["دیجیکالا", "بامیلو" , "بامیلو" , "بامیلو" , "بامیلو" , "بامیلو"]})




def search_view(request):
    a = filter(
        50000,
        10000000000,
        30,
        60,
        0,
        50000000000,
        ['DigikalaIds'],
        "Aerobic"
    )
    s=''
    for i in a:
        s += "<div>" + i.url + "</div>"
    return HttpResponse(s)

def favicon(request):
    return HttpResponse("salam")
