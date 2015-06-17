# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#project: w3school
#file   : items.py
#author : younghz
#brief  : define W3schoolItem.

# import scrapy
from scrapy.item import Item,Field

class W3SchoolItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    link = Field()
    desc = Field()
    # pass
