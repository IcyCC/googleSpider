# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoogleimagItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    keyword = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
    describe = scrapy.Field()
    id = scrapy.Field()
