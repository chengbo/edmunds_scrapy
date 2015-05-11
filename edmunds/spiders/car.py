# -*- coding: utf-8 -*-
import scrapy
from edmunds.items import *

class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["www.edmunds.com"]
    start_urls = (
        'http://www.edmunds.com/bmw/m6-gran-coupe/2015/st-200695680/features-specs/',
    )

    def parse(self, response):
        item = EdmundsItem()
        item['highlights'] = self.parseHighlights(response)
        item['colors'] = self.parseColors(response)

        return item

    def parseColors(self, response):
        item = ColorItem()
        item['exterior'] = []
        item['interior'] = []
        section = response.xpath('//div[@id="colors-pod"]')

        i_elements = section.xpath('//span[re:test(@id, "exterior_\d$")]')
        for e in i_elements:
            color = e.xpath('span[@class="clrtxt"]/text()').extract()[0]
            item['exterior'].append(color)

        e_elements = section.xpath('//span[re:test(@id, "exterior_\d$")]')
        for e in e_elements:
            color = e.xpath('span[@class="clrtxt"]/text()').extract()[0]
            item['interior'].append(color)

        return item

    def parseHighlights(self, response):
        items = []
        elements = response.xpath('//div[@id="highlights-pod"]//li')
        for e in elements:
            item = HighlightItem()
            item['key'] = e.xpath('span/text()').extract()[0]
            item['value'] = e.xpath('em/text()').extract()[0]
            items.append(item)

        return items


