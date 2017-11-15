# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.loader import ItemLoader
from scrapy_splash import SplashRequest
from ORM_app.models import TorobShopId

class Torob2Spider(scrapy.Spider):
    name = 'torob_urls'
    url = 'https://api.torob.com/android-api/3/special-offers/?limit=20&page=1'
    start_urls = [url + '1']

    def parse(self, response):
        data = json.loads(response.text)
        for i in range(0,len(data['result'])):
            id = TorobShopId(shopid = int(data['result'][i]['data'][0]['shop_id']))
            id.save()


        for i in range(1,50):
            next_page = self.url + str(i)
            yield scrapy.Request(url=next_page, callback=self.parse)
