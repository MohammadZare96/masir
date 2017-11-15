# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ORM_app.models import *


class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['torob.com']
    start_urls = ['http://torob.com/']

    def start_requests(self):
        for i in range(1, 501):
            yield Request(url="https://torob.com/browse/"+str(i), callback=self.parse)

    def parse(self, response):
        a = response.url.split("/")
        cat = Category(
            category = a[5],
            pid = a[4]
        )
        cat.save()
