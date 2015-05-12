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
        item['specifications'] = self.parseSpecifications(response)

        return item

    def parseSpecifications(self, response):
        def buildXpath(i):
            return './following-sibling::table \
                    [1 = count(preceding-sibling::h3[1] | ../h3[%d])]' % (i + 1)

        specs = []
        elements = response.xpath('//div[@id="specification-pod"]//h3')
        for i in range(0, len(elements)):
            item = KeyValueItem()
            item['key'] = elements[i].xpath('text()').extract()
            item['value'] = self.parseTable(elements[i].xpath(buildXpath(i)))

            specs.append(item)

        return specs

    def parseTable(self, table):
        items = []
        li_list = table.xpath('.//li')
        if len(li_list) > 0:
            for li in li_list:
                items.append(li.xpath('span/text()').extract())
        else:
            label_list = table.xpath('.//label')
            for label in label_list:
                innerItem = KeyValueItem()
                innerItem['key'] = label.xpath('text()').extract()
                innerItem['value'] = label.xpath('./following-sibling::span/text()').extract()
                items.append(innerItem)

        return items

    def parseColors(self, response):
        item = ColorItem()
        item['exterior'] = []
        item['interior'] = []
        section = response.xpath('//div[@id="colors-pod"]')

        i_elements = section.xpath('.//span[re:test(@id, "exterior_\d$")]')
        for e in i_elements:
            color = e.xpath('span[@class="clrtxt"]/text()').extract()[0]
            item['exterior'].append(color)

        e_elements = section.xpath('.//span[re:test(@id, "exterior_\d$")]')
        for e in e_elements:
            color = e.xpath('span[@class="clrtxt"]/text()').extract()[0]
            item['interior'].append(color)

        return item

    def parseHighlights(self, response):
        items = []
        elements = response.xpath('//div[@id="highlights-pod"]//li')
        for e in elements:
            item = KeyValueItem()
            item['key'] = e.xpath('span/text()').extract()[0]
            item['value'] = e.xpath('em/text()').extract()[0]
            items.append(item)

        return items


