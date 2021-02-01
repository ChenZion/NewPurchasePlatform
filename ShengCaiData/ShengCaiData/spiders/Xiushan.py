import scrapy


class XiushanSpider(scrapy.Spider):
    name = 'Xiushan'
    allowed_domains = ['xiushanfuwu']
    start_urls = ['http://xiushanfuwu/']

    def parse(self, response):
        pass
