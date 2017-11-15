# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy_splash import SplashRequest

# from ORM_project.ORM_app.models import Torob
from ORM_app.models import Torob



class QuotesSpider(scrapy.Spider):
    name = 'torob'
    def start_requests(self):
        main_url = 'https://torob.com/special-offers/{}'
        yield SplashRequest(
            url = main_url.format(1),
            callback=self.parse,
        )
    # allowed_domains = ['torob.com']
    # start_urls = ['https://torob.com/special-offers/10/%D8%AF%DB%8C%D8%AC%DB%8C%DA%A9%D8%A7%D9%84%D8%A7']

    def parse(self, response):
        main_url = 'https://torob.com/special-offers/{}'
        self.log("i just visit: " + response.url)
        address = response.selector.xpath('//a[contains(@class, "boxify fixed-card")]/@href').extract()
        discount = response.selector.xpath('//div[contains(@class, "discount-percent")]/text()').extract()
        del discount[1::2]
        oldprice= response.selector.xpath('//div[contains(@class, "text-center") and contains(@class ,"price") and contains(@class, "line-through")]/text()').extract()
        del oldprice[1::2]
        for i in range(0, len(oldprice)):
            oldprice[i]=int(re.sub(",", "", oldprice[i]))
        newprice = response.selector.xpath('//div[contains(@class, "text-center") and contains(@class ,"price") and not(contains(@class, "line-through"))]/text()').extract()
        del newprice[1::2]
        for i in range(0, len(newprice)):
            newprice[i]=int(re.sub(",", "", newprice[i]))



        url_join = "https://torob.com"
        item_name = response.css('h5.title-main::text').extract()
        new_price = newprice
        old_price = oldprice
        discount_percent = discount
        address = address
        print len(item_name), len(new_price), len(old_price), len(discount_percent), len(address)
        for i in range(0,len(item_name)):
            url = url_join + address[i]
            # print url
            item = Torob(item_name = item_name[i], new_price=new_price[i], old_price=old_price[i], discount_price =old_price[i]-new_price[i] , discount_percent=discount_percent[i], address=url)
            # item = TorobIds(url=url)
            item.save()

        # urls = response.selector.xpath('//*[@id="__next"]/div/div/div/div/div/div/div/div/div/h3/div/div/a/@href').extract()
        for i in range(0,200):
            next_url = main_url.format(i)
            yield scrapy.Request(url = next_url, callback=self.parse)
