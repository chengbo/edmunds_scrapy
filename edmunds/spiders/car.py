# -*- coding: utf-8 -*-
import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["www.edmunds.com"]
    start_urls = (
        'http://www.www.edmunds.com/',
    )

    def parse(self, response):
        pass
