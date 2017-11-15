# -*- coding: utf-8 -*-
import scrapy

from ORM_app.models import DigikalaUrlsL1,DigikalaUrlsL2
from scrapy import Request


class DigikalaUrlL2Spider(scrapy.Spider):
    name = 'digikala_url_l2'
    allowed_domains = ['digikala.com']

    l1_urls = DigikalaUrlsL1.objects.filter()
    def start_requests(self):
        urls = DigikalaUrlsL1.objects.filter()
        start_urls = []
        for url in urls:
            start_urls.append(url.url)
        for i in range(0,len(start_urls)):
            yield Request(url=start_urls[i].replace('https://', 'http://'), callback=self.parse)

    def parse(self, response):
        next_url = response.selector.xpath('//*[@id="menu"]/ul/div/li/ul/li/a/@href').extract()
        for i in range(0, len(self.l1_urls)):
            if self.l1_urls[i].url.replace('https://', 'http://') == response.url:
                category1 = self.l1_urls[i].category1
        for url in next_url:
            item = DigikalaUrlsL2(
                url='https://www.digikala.com'+url,
                category1=category1,
                category2=url.split('/')[-2][9:] if "Category" in url else url.split('/')[-2]
            )
            item.save()

