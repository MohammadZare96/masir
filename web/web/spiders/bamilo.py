# -*- coding: utf-8 -*-

import sys
import urllib

reload(sys)
sys.setdefaultencoding('utf8')
import datetime
import json

import django
import re
import scrapy
from ORM_app.models import Product_Bamilo, BamiloIds, Masir
from scrapy import Request
from scrapy_splash import SplashRequest

from ORM_app.category import bamilo_categorize

# Product_Bamilo.objects.all().delete()
# Masir.objects.all().delete()

class BamiloSpider(scrapy.Spider):
    name = 'bamilo'
    allowed_domains = ['bamilo.com']
    start_urls = ['http://bamilo.com/']
    urls = BamiloIds.objects.filter()
    start_urls = []
    for url in urls:
        start_urls.append(url.url)
    def start_requests(self):
        # start_urls = ['https://www.digikala.com/Product/DKP-284023/']

        # for url in start_urls:
        #     print url
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)
            # yield self.make_requests_from_url(url)

    def parse(self, response):

        #print self.start_urls.index(response.url)
        # item_name = response.selector.xpath('//section[contains(@class, "sku-detail")]/div[contains(@class, "details-wrapper")]/div[contains(@class, "details -validate-size")]/span[contains(@itemprop, "name")]/h1/text()').extract()
        # item_name = self.check_name(item_name)
        new_price = response.selector.xpath('//section[contains(@class, "sku-detail")]/div[contains(@class, "details-wrapper")]/div[contains(@class, "details -validate-size")]/div[contains(@class, "details-footer")]/div[contains(@class, "price-box")]/span[contains(@class, "price") and not(contains(@class, "price -old"))]/span/@data-price').extract()
        new_price = self.check_price(new_price)
        new_price = int(new_price)
        old_price = response.selector.xpath('//section[contains(@class, "sku-detail")]/div[contains(@class, "details-wrapper")]/div[contains(@class, "details -validate-size")]/div[contains(@class, "details-footer")]/div[contains(@class, "price-box")]/span[contains(@class, "price -old")]/span/@data-price').extract()
        old_price = self.check_price(old_price)
        old_price = int(old_price)
        item_image = response.selector.xpath('//*[@id="productImage"]/@data-src').extract_first()
        # classification = response.selector.xpath('//main[contains(@class, "osh-container")]/nav[contains(@class, "osh-breadcrumb")]/ul/li[2]/a/@href').extract_first()
        # classification = classification.rsplit('/',2)[1]
        # classification_1 = response.selector.xpath(
        #     '//main[contains(@class, "osh-container")]/nav[contains(@class, "osh-breadcrumb")]/ul/li[3]/a/@href').extract_first()
        # if classification_1 is None:
        #     classification_1 = ''
        # else:
        #     classification_1 = classification_1.rsplit('/', 2)[1]
        # classification_2 = response.selector.xpath(
        #     '//main[contains(@class, "osh-container")]/nav[contains(@class, "osh-breadcrumb")]/ul/li[4]/a/@href').extract_first()
        # if classification_2 is None:
        #     classification_2 = ''
        # else:
        #     classification_2 = classification_2.rsplit('/', 2)[1]



        P = response.text.split('jsTrackingStore.data = ')[1].split('jsTrackingStore.merge')[0].rstrip()
        P = re.sub(";", "", P)
        P = json.loads(P)
        details1 = P['products'][P['products'].keys()[0]]
        item_name = details1['name']
        cat = details1['category']

        cat = re.sub('"', '', cat)
        cat = cat.split('/')
        try:
            categoryfa = cat[0]
        except:
            categoryfa = ''
        try:
            categoryfa1 = cat[1]
        except:
            categoryfa1 = ''
        try:
            categoryfa2 = cat[2]
        except:
            categoryfa2 = ''
        try:
            categoryfa3 = cat[3]
        except:
            categoryfa3 = ''
        try:
            categoryfa4 = cat[4]
        except:
            categoryfa4 = ''




        brand = details1['brand']
        # category1 = P['dataLayer']['biCat1name']
        # category2 = P['dataLayer']['biCat2name']
        # category3 = P['dataLayer']['biCat3name']

        try:
            category1 = response.selector.xpath('//main/nav/ul/li[2]/a/@href').extract_first().rsplit('/')[-2]
        except:
            category1 = ''
        try:
            category2 = response.selector.xpath('//main/nav/ul/li[3]/a/@href').extract_first().rsplit('/')[-2]
        except:
            category2 = ''
        try:
            category3 = response.selector.xpath('//main/nav/ul/li[4]/a/@href').extract_first().rsplit('/')[-2]
        except:
            category3 = ''
        try:
            category4 = response.selector.xpath('//main/nav/ul/li[5]/a/@href').extract_first().rsplit('/')[-2]
        except:
            category4 = ''
        try:
            category5 = response.selector.xpath('//main/nav/ul/li[6]/a/@href').extract_first().rsplit('/')[-2]
        except:
            category5 = ''

        discount_price = 0 if old_price==0 else old_price - new_price
        bamilo = Product_Bamilo(
            item_name=item_name,
            new_price = new_price,
            old_price = old_price,
            discount_price = discount_price,
            discount_percent = 0 if old_price==0 else (old_price - new_price)*100/old_price,
            address = response.url,
            item_image = item_image,
            categoryfa = categoryfa,
            categoryfa1 = categoryfa1,
            categoryfa2 = categoryfa2,
            categoryfa3 = categoryfa3,
            categoryfa4 = categoryfa4,
            category1 = category1,
            category2 = category2,
            category3 = category3,
            category4 = category4,
            category5 = category5,
            brand = brand,
            time = django.utils.timezone.now()
        )

        p = BamiloIds.objects.filter(url=urllib.unquote(response.url).decode('utf8'))[0]
        # for p in BamiloIds.objects.filter():
        #     if urllib.unquote(response.url).decode('utf8') == p.url.decode("utf-8"):
        #         print urllib.unquote(response.url).decode('utf8') == p.url.decode("utf-8")
        #         category1 = p.category1
        #         category2 = p.category2
        # print(BamiloIds.objects.filter(url=response.url.decode("utf-8")))
        # p = BamiloIds.objects.filter(url=response.url.decode("utf-8"))[0]

        bamilo.masir_cat = bamilo_categorize(p.category1, p.category2)
        if discount_price != 0:
            bamilo.save()

        masir = Masir(
            item_name=item_name,
            new_price=new_price,
            old_price=old_price,
            discount_price=discount_price,
            discount_percent=0 if old_price == 0 else (old_price - new_price) * 100 / old_price,
            address=response.url,
            item_image=item_image,
            brand=brand,
            time=django.utils.timezone.now()
        )
        masir.masir_cat = bamilo_categorize(p.category1, p.category2)
        if discount_price != 0:
            masir.save()



    def check_name(self, name):
        if len(name) == 0:
            return ''
        else:
            return name[0]
    def check_price(self, name):
        if len(name) == 0:
            return '0'
        else:
            return name[0]
