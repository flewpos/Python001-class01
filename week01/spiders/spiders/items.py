# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    movieName = scrapy.Field()
    movieType = scrapy.Field()
    movieShowTime = scrapy.Field()
    pass
