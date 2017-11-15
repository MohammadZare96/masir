# -*- coding: utf-8 -*-
import scrapy

from ORM_app.models import BamiloUrlsL1, BamiloUrlsL2
from scrapy import Request


class BamiloUrlL2Spider(scrapy.Spider):
    name = 'bamilo_url_l2'
    allowed_domains = ['bamilo.com']
    # start_urls = ['http://bamilo.com/']
    l1_urls = BamiloUrlsL1.objects.filter()
    def start_requests(self):
        # start_urls = ['https://www.digikala.com/Product/DKP-284023/']
        urls = BamiloUrlsL1.objects.filter()
        start_urls = []
        for url in urls:
            start_urls.append(url.url)
        # for url in start_urls:
        #     print url
        for i in range(0,len(start_urls)):
            yield Request(url=start_urls[i], callback=self.parse)

    def parse(self, response):
        next_url = response.selector.xpath('//main/aside/section[1]/ul/li/a/@href').extract()
        for i in range(0, len(self.l1_urls)):
            if response.url == self.l1_urls[i].url:
                category1 = self.l1_urls[i].category1
        for url in next_url:
            item = BamiloUrlsL2(
                url=url,
                category1=category1,
                category2=url.split('/')[-2]
            )
            item.save()