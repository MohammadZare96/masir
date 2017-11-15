# -*- coding: utf-8 -*-
import datetime

import django
import scrapy
from scrapy.linkextractors import LinkExtractor

from ORM_app.models import BamiloIds, BamiloUrlsL2

# BamiloIds.objects.all().delete()
class BamiloSpider(scrapy.Spider):
    name = 'bamilo_id'
    allowed_domains = ['bamilo.com']
    flag = 0
    all_urls = BamiloUrlsL2.objects.all()
    start_urls = ['http://www.bamilo.com']
    count = 0
    def parse(self, response):

        # item_name = response.selector.xpath('//a/h2/span[contains(@class, "name")]/text()').extract()
        # new_price =  response.selector.xpath('//span[contains(@class, "price-box")]/span[contains(@class, "price") and not(contains(@class, "price -old"))]/span[contains(@dir, "ltr")][1]/@data-price').extract()
        # old_price =  response.selector.xpath('//span[contains(@class, "price-box")]/span[contains(@class, "price -old")]/span[contains(@dir, "ltr")][1]/@data-price').extract()
        address =  response.selector.xpath('//section[contains(@class, "products")]/div[contains(@class, "sku -gallery")]/a[1]/@href').extract()

        # new_price=map(float, new_price)
        # old_price=map(float, old_price)+

        last_urls = []
        last_products = BamiloIds.objects.values_list('url').filter(flag=1)
        for p in last_products:
            last_urls.append(p[0])
        print response.url , self.all_urls[0].url
        category1 = 'None'
        category2 = 'None'
        for i in range(0 , len(self.all_urls)):
            if self.all_urls[i].url in response.url:
                category1 = self.all_urls[i].category1
                category2 = self.all_urls[i].category2
        for i in range(0,len(address)):
            # item = Bamilo(item_name = item_name[i], new_price=int(round(new_price[i])), old_price=int(round(old_price[i])), discount_price =old_price[i]-new_price[i] , discount_percent=(old_price[i]-new_price[i])*100/old_price[i], address=address[i])
            if address[i] in last_urls:
                self.flag=1
                break
            else:
                item = BamiloIds(
                    url=address[i],
                    time=django.utils.timezone.now(),
                    category1=category1,
                    category2=category2
                )
                if ("page=" not in response.url) and (i == 0):
                    item.flag = 1
                else:
                    item.flag = 0
                item.save()


####################### find all next links in a specific page and after that jupm to new url in all urls #########
        next_url = response.selector.xpath('//ul[contains(@class , "osh-pagination -horizontal")]/li[contains(@class , "item")]/a[contains(@rel , "next")]/@href').extract()
        if (len(next_url) == 0 or self.flag==1):
            # all_urls = response.selector.xpath('//ul[contains(@class, "submenu")]/li/a/@href').extract()[4:]
            # print all_urls, "\n\n\n\n\n\n\n\n\n"
            # label : next
            self.flag=0
            try:
                yield scrapy.Request(url=self.all_urls[self.count].url, callback=self.parse)
            except:
                pass
            self.count+=1

        elif len(next_url) > 0:
            yield scrapy.Request(url=next_url[0], callback=self.parse)
