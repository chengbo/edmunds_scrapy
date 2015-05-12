# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EdmundsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    highlights = scrapy.Field()
    colors = scrapy.Field()
    specifications = scrapy.Field()
    features = scrapy.Field()

class KeyValueItem(scrapy.Item):
    key = scrapy.Field()
    value = scrapy.Field()

class ColorItem(scrapy.Item):
    exterior = scrapy.Field()
    interior = scrapy.Field()
