# -*- coding: utf-8 -*-
import scrapy

from ORM_app.models import BamiloUrlsL1

class BamiloUrlL1Spider(scrapy.Spider):
    name = 'bamilo_url_l1'
    allowed_domains = ['bamilo.com']
    start_urls = ['http://www.bamilo.com']
    all_urls = [
        'http://www.bamilo.com/men_clothes/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/women_clothes/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        ,'http://www.bamilo.com/mens_shoes/?source=gfm'
        ,'http://www.bamilo.com/women_shoes/?source=gfm'
        ,'http://www.bamilo.com/women_bags_wallets/?source=gfm'
        ,'http://www.bamilo.com/men_bags_wallets_covers/?source=gfm'
        , 'http://www.bamilo.com/fashion_men_accessories/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/fashion_women_accessories/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/kidsfashion/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/luggages-bags/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/smartphone_tablet_mobile/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/electronic_accessories/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        ,
        'http://www.bamilo.com/computer_office_equipment_printer_scanner/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        ,
        'http://www.bamilo.com/camera_equipment_photography_imaging/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        ,
        'http://www.bamilo.com/tv_entertainment_game_console_camera/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/console_gaming/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/kitchen_kitchenware/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/house_general_goods/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/home-decorating/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/bedroom_bed_furniture/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/cleaning_dusting/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/home_appliance/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/kitchen_appliance/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/perfumes/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/skin_care/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/hand_feet_nails/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/makeup/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/oral_care/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/hair_care/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/shaving_grooming/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/human_health/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/toddler/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/men_sportswear/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/women_sportswear/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/sports_apparel/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/camping-climbing/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/sports-outdoors/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/toys_main/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/books_main/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/stationery/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/multimedia/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/home_living_handcrafts/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/tools-parent/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/car_equipment/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/drinks/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/junk-food/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/breakfast/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/spice/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/cleaning_dusting/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
        , 'http://www.bamilo.com/pet-shop/?facet_is_mpg_child=0&viewType=gridView&sort=newest&dir=desc'
    ]

    def parse(self, response):
        for url in self.all_urls:
            item = BamiloUrlsL1(url=url, category1=url.split('/')[3])
            item.save()
