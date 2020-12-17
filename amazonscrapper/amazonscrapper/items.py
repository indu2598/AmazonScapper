# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # We are going to fetch these items from the site
    product_name = scrapy.Field()
    product_author = scrapy.Field()
    product_price = scrapy.Field()
    product_imageLink = scrapy.Field()

