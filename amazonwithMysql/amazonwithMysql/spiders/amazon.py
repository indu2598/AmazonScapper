import scrapy
from ..items import AmazonwithmysqlItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    page_number = 2
    start_urls = ['https://www.amazon.in/gp/bestsellers/books/ref=nav_ya_signin?ie=UTF8&pg=1&']

    def parse(self, response):
        myitems = AmazonwithmysqlItem()
        myitems['product_name'] = response.css('#zg-ordered-list img::attr(alt)').extract()
        myitems['product_author'] = response.css('.a-link-child::text').extract()
        myitems['product_price'] = response.css('.p13n-sc-price::text').extract()
        myitems['product_imageLink'] = response.css('#zg-ordered-list img::attr(src)').extract()
        yield myitems

        next_page = 'https://www.amazon.in/gp/bestsellers/books/ref=nav_ya_signin?ie=UTF8&pg=' + str(
            AmazonSpider.page_number) + '&'
        if AmazonSpider.page_number <= 2:
            AmazonSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

