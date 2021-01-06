# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class ToutiaoItem(scrapy.Item):
    PageUrl = scrapy.Field()
    TitleXpath = scrapy.Field()
    Title = scrapy.Field()

