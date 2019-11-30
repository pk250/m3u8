# -*- coding: utf-8 -*-
import scrapy


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['http://bilibili.com/']

    def parse(self, response):
        pass
