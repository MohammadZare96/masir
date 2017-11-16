# -*- coding: utf-8 -*-
import json
import re

import django
import scrapy
from ORM_app.models import Digikala_details, Product_Digikala, Masir
from ORM_app.category import digikala_categorize
from scrapy import Request
from scrapy_splash import SplashRequest
import datetime
# Masir.objects.all().delete()



# p = Product_Digikala.objects.filter(masir_cat = 'Digital-Accessories')
# i = 1
# for item in p:
#     print i
#     i+=1
#     Product_Digikala.objects.filter(item_name = item.item_name, item_persian_name = item.item_persian_name).exclude(masir_cat = item.masir_cat).delete()




class DigikalaSpider(scrapy.Spider):
    name = 'digikala'
    allowed_domains = ['digikala.com', 'localhost', 'https://www.digikala.com', 'www.digikala.com']

    # for url in urls:
    #     start_urls_temp.append(url.address)
    def start_requests(self):
        urls = Product_Digikala.objects.all()
        start_urls = []
        for url in urls:
            start_urls.append(url.address)
        # for url in start_urls:
        #     print url
        i = 1
        for url in start_urls:
            print i
            i+=1
            yield Request(url=url, callback=self.parse)
        # yield self.make_requests_from_url(url)
    # count = 0
    # try:
    #     start_urls = [start_urls_temp[0]]
    # except:
    #     pass

    #
    # def start_requests(self):
    #     # start_urls = ['https://www.digikala.com/Product/DKP-284023/']
    #     urls = DigikalaIds.objects.all()
    #     start_urls = []
    #     for url in urls:
    #         start_urls.append(url.url)
    #     # for url in start_urls:
    #     #     print url
    #     for url in start_urls:
    #         # yield Request(url=url, callback=self.parse)
    #         yield SplashRequest(url=url, callback=self.parse, args={'wait': 2, 'timeout': 90})
    #         # yield self.make_requests_from_url(url)

    def parse(self, response):

        # item_persian_name = response.selector.xpath('//div[contains(@class, "products-info")]/header[contains(@class, "clearfix")]/div[contains(@class, "info-header")]/h1/text()').extract()
        # item_persian_name = self.check_name(name=item_persian_name)
        # item_english_name = response.selector.xpath('//div[contains(@class, "products-info")]/header[contains(@class, "clearfix")]/div[contains(@class, "info-header")]/h1/span/text()').extract()
        # item_english_name = self.check_name(name=item_english_name)
        # new_price = response.selector.xpath('//div[contains(@class, "products-info")]/div[contains(@class, "products-config clearfix")]/div[contains(@class, "config-right")]/div[contains(@id, "frmPnlProductConfigR_Content")]/div[contains(@id, "products-price-status")]/div[contains(@id, "frmPnlPayablePrice")]/span[contains(@id, "frmLblPayablePriceAmount")]/text()').extract()
        # new_price = self.check_price(name=new_price)
        # new_price = int(re.sub(",", "", new_price))
        # old_price = response.selector.xpath('//div[contains(@class, "products-info")]/div[contains(@class, "products-config clearfix")]/div[contains(@class, "config-right")]/div[contains(@id, "frmPnlProductConfigR_Content")]/div[contains(@id, "products-price-status")]/div[contains(@id, "frmPnlPrice")]/span[contains(@id, "frmLblPriceAmount")]/text()').extract()
        # old_price = self.check_price(name=old_price)
        # old_price = int(re.sub(",", "", old_price))

        P = response.text.split('ecpd2.brand = ')[1].split('ecpd2.category')[0]
        P = re.sub("\r\n", "", P)
        P = re.sub(";", "", P)
        P = re.sub(" ", "", P)
        P = re.sub("id:", '"id":', P)
        P = re.sub(",fa:", ',"fa":', P)
        P = re.sub(",en:", ',"en":', P)
        P = json.loads(P)
        brand_fa = P['fa']
        brand = P['en']
        #
        # cat = response.selector.xpath('//*[@id="dk-breadcrumbs"]/ol/li[4]/a/@href').extract_first()
        # category_2 = cat.rsplit('/')[-1] if cat.rsplit('/')[-1] != '' else cat.rsplit('/')[-2]


        # P = response.text.split('ecpd2.breadCrums = ')[1].split('.split("/")')[0]
        # P = re.sub('"', '', P)
        # P = P.split('/')
        # try:
        #     category = P[0]
        # except:
        #     category = ''
        # try:
        #     category1 = P[1]
        # except:
        #     category1 = ''
        # try:
        #     category2 = P[2]
        # except:
        #     category2 = ''
        # try:
        #     category3 = P[3]
        # except:
        #     category3 = ''
        product_id = response.url.split('/')[4][4:]
        # digikala = Digikala_details(
        #     # item_persian_name = "unavailable" if item_persian_name == '' else item_persian_name,
        #     # item_english_name = item_english_name,
        #     # new_price = new_price,
        #     # old_price = old_price,
        #     # discount_price = 0 if old_price==0 else old_price - new_price,
        #     # discount_percent = 0 if old_price==0 else (old_price - new_price)*100/old_price,
        #     # address = response.url,
        #     product_id=product_id,
        #     brand=brand,
        #     brand_fa=brand_fa,
        #     # category = category,
        #     # category1 = category1,
        #     # category2 = category2,
        #     # category3 = category3,
        #     time=django.utils.timezone.now()
        # )
        # # digikala.masir_cat = cattegory([
        # #     Product_Digikala.objects.filter(product_id=product_id)[0].item_name,
        # #     Product_Digikala.objects.filter(product_id=product_id)[0].item_persian_name,
        # #     Product_Digikala.objects.filter(product_id=product_id)[0].category,
        # #     category,
        # #     category1,
        # #     category2,
        # #     category3
        # #     ]
        # # )
        # digikala.save()

        # print category_2
        # Product_Digikala.objects.filter(product_id = product_id).update(
        #     brand=brand,
        #     brand_fa=brand_fa,
        #     category2=category_2
        # )
        products = Product_Digikala.objects.filter(product_id = product_id)
        for p in products:
            p.brand=brand,
            p.brand_fa=brand_fa,
            p.masir_cat = digikala_categorize(p.category1, p.category2)
            masir = Masir(
                item_name=p.item_name if p.item_name != '' else p.item_persian_name,
                new_price = p.new_price,
                old_price = p.old_price,
                discount_price = p.discount_price,
                discount_percent = p.discount_percent,
                address = p.address,
                item_image = p.item_image,
                masir_cat = digikala_categorize(p.category1, p.category2),
                brand = brand,
                time = p.time
            )
            masir.save()
            p.save()



        # self.count += 1
        # yield Request(url=self.start_urls_temp[self.count], callback=self.parse)

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