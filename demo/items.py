# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class ProfItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    email = scrapy.Field()
    org = scrapy.Field()
    type = scrapy.Field()
    judge = scrapy.Field()
