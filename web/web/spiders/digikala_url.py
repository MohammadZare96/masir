# -*- coding: utf-8 -*-
import json

import re

import datetime

import django
import scrapy
from ORM_app.models import DigikalaUrls


# DigikalaUrls.objects.all().delete()
class DigikalaSpider(scrapy.Spider):
    name = 'digikala_url'
    allowed_domains = ['digikala.com']
    start_urls = ['https://www.digikala.com']




    def parse(self,response):
        l_two_urls = response.selector.xpath('//*[@id="dkForm"]/nav/div/div/ul/li/ul/li/a/@href').extract()
        for url in l_two_urls:
            if url.rsplit('/')[-3] =='Search':
                link = DigikalaUrls(url = "https://digikala.com"+url, time = django.utils.timezone.now())
                link.save()
            else:
                link = DigikalaUrls(url = "https://digikala.com/Search/Category-"+url.rsplit('/')[-2]+'/', time = django.utils.timezone.now())
                link.save()





