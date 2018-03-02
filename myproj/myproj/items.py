# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class MainList(scrapy.Item):
    title = Field()
    sublist = Field()

class SubList(scrapy.Item):
    title = Field()
    url = Field()

"""
{
    "title": "Animals",
    "sublist": [
        {
            "title": 'Subitem'
            "url": "http://foo.com"
        },
        {
            "title": 'Subitem'
            "url": "http://foo.com"
        },
    ]

}

items = []
for titles in titles:
    item = MainList()
    item['title']
"""