# -*- coding: utf-8 -*-
import scrapy


class HuyaSpider(scrapy.Spider):
    name = 'huya'
    allowed_domains = ['huya.com']
    start_urls = ['http://huya.com/']

    def parse(self, response):
        pass
