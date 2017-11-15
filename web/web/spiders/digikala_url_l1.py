# -*- coding: utf-8 -*-
import django
import scrapy

from ORM_app.models import DigikalaUrlsL1


class DigikalaUrlL1Spider(scrapy.Spider):
    name = 'digikala_url_l1'
    allowed_domains = ['digikala.com']
    start_urls = ['http://digikala.com/']

    def parse(self,response):
        l_1_urls = response.selector.xpath('//nav/div/div/ul/li/ul/li/a/@href').extract()
        for url in l_1_urls:
            link = DigikalaUrlsL1(url = "http://www.digikala.com"+url, category1=url.rsplit('/')[-2])
            link.save()
