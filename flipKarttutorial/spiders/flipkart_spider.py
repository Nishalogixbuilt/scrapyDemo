from gc import callbacks
import scrapy
from ..items import FlipkarttutorialItem

class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'   
    page_number = 2
    start_urls = [
        'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi&otracker=nmenu_sub_Electronics_0_Mi'
        ]

    def parse(self, response):
        items = FlipkarttutorialItem()
        product_name = response.css('._4rR01T::text').extract()
        product_price = response.css('._1_WHN1::text').extract()
        product_imagelink = response.css('._396cs4::attr(src)').extract()
        

        items['product_name']  = product_name
        items['product_price']  = product_price
        items['product_imagelink']  = product_imagelink

        yield items

        next_page = 'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&otracker=nmenu_sub_Electronics_0_Mi&page='+ str(FlipkartSpiderSpider.page_number)

        if FlipkartSpiderSpider.page_number<=17:
            FlipkartSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)