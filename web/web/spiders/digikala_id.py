# -*- coding: utf-8 -*-
import json

import re

import datetime
from ORM_app.category import digikala_category
import django
import scrapy
from ORM_app.models import Product_Digikala, DigikalaUrlsL2

# Product_Digikala.objects.all().delete()


class DigikalaSpider(scrapy.Spider):
    max_pages = 200

    name = 'digikala_id'
    allowed_domains = ['digikala.com']
    count = 0
    # urls = DigikalaUrls.objects.values_list('url').distinct()
    urls = DigikalaUrlsL2.objects.all().exclude(
        url__in=[
            'https://www.digikala.com/Main/Electronic-Devices/Accessories-Main/Mobile-Accessories/',
            'https://www.digikala.com/Main/Electronic-Devices/Accessories-Main/Tablet-Accessories/',
            'https://www.digikala.com/Main/Electronic-Devices/Accessories-Main/Laptop-Accessories/',
            'https://www.digikala.com/Main/Electronic-Devices/Accessories-Main/Camera-Accessories/',
            'https://www.digikala.com/Search/Category-Computer-Accessories/#!/Category-Electronic-Devices/Category-Accessories-Main/Category-Computer-Accessories/',
            'https://www.digikala.com/Search/Category-Office-Accessories/#!/Category-Electronic-Devices/Category-Accessories-Main/Category-Office-Accessories/'
        ]
    )
    new_urls = []
    category1 = []
    category2 = []
    for i in range(0, len(urls)):
        for j in range(0, max_pages):
            if 'Category' in urls[i].url:
                new_urls.append('https://search.digikala.com/api/SearchApi/?urlCode=' + urls[i].url.rsplit('/', 2)[-2][
                    9:] + '&pageno=' + str(j) + '&pageSize=40')
                category1.append(urls[i].category1)
                category2.append(urls[i].category2)
            else:
                new_urls.append('https://search.digikala.com/api/SearchApi/?urlCode=' + urls[i].url.rsplit('/', 2)[
                    -2] + '&pageno=' + str(j) + '&pageSize=40')
                category1.append(urls[i].category1)
                category2.append(urls[i].category2)
    try:
        start_urls = ['https://search.digikala.com/api/SearchApi/?urlCode=' + urls[0].url.rsplit('/', 2)[-2][
                                                                              9:] + '&pageno=0&pageSize=40']
    except:
        pass

    def parse(self, response):
        self.log("i just visit: " + response.url)
        data = json.loads(response.text)
        category = response.url.split('https://search.digikala.com/api/SearchApi/?urlCode=')[1].split('&')[0]
        for i in range(0, len(data['hits']['hits'])):
            item_persian_name = data['hits']['hits'][i]['_source']['FaTitle']
            item_persian_name = self.check_name(name=item_persian_name)
            item_name = data['hits']['hits'][i]['_source']['EnTitle']
            item_name = self.check_name(name=item_name)
            new_price = data['hits']['hits'][i]['_source']['MinPrice']
            if (data['hits']['hits'][i]['_source']['MinPrice'] == 0 and data['hits']['hits'][i]['_source'][
                'MaxPrice'] == 0 and data['hits']['hits'][i]['_source']['MinPriceList'] == 0):
                self.count = self.max_pages - self.count % self.max_pages + self.count
                print self.count
                break

            old_price = data['hits']['hits'][i]['_source']['MinPriceList']
            discount_price = 0 if old_price == 0 else old_price - new_price

            address = 'https://www.digikala.com/Product/DKP-' + str(data['hits']['hits'][i]['_id'])
            image_url = "https://file.digi-kala.com/digikala/" + data['hits']['hits'][i]['_source']['ImagePath']
            item = Product_Digikala(
                address=address,
                item_persian_name="unavailable" if item_persian_name == '' else item_persian_name,
                item_name=item_name,
                new_price=new_price,
                old_price=old_price,
                discount_price=discount_price,
                discount_percent=0 if old_price == 0 else (old_price - new_price) * 100 / old_price,
                item_image=image_url,
                category1=self.category1[self.count],
                category2=self.category2[self.count],
                product_id=data['hits']['hits'][i]['_id'],
                time=django.utils.timezone.now(),
                # masir_cat=digikala_category(category)
            )
            if (new_price is not 0 and discount_price is not 0):
                item.save()

        if len(self.new_urls) > self.count:
            yield scrapy.Request(url=self.new_urls[self.count], callback=self.parse, dont_filter=True)
            self.count += 1

    def check_name(self, name):
        if len(name) == 0:
            return ''
        else:
            return name

            # def check_price(self, name):
            #     if len(name) == 0:
            #         return '0'
            #     else:
            #         return name
            #
