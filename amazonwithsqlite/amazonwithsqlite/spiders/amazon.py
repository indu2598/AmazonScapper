import scrapy
from ..items import AmazonwithsqliteItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    page_number = 2
    start_urls = ['https://www.amazon.in/gp/bestsellers/books/ref=nav_ya_signin?ie=UTF8&pg=1&']


    def parse(self, response):
        myitems = AmazonwithsqliteItem()
        full_items = response.css('.zg-item')
        for item in full_items[0:3]:
            myitems['product_name'] = item.css('#zg-ordered-list img::attr(alt)').extract()
            myitems['product_author'] = item.css('.a-link-child::text').extract()
            myitems['product_price'] = item.css('.p13n-sc-price::text').extract()
            myitems['product_imageLink'] = item.css('#zg-ordered-list img::attr(src)').extract()
        yield myitems

        next_page = 'https://www.amazon.in/gp/bestsellers/books/ref=nav_ya_signin?ie=UTF8&pg=' + str(
            AmazonSpider.page_number) + '&'
        if AmazonSpider.page_number <= 2:
            AmazonSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)