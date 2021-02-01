import scrapy


class DianxinzengzhiSpider(scrapy.Spider):
    name = 'Dianxinzengzhi'
    allowed_domains = ['dianxinzengzhi']
    start_urls = ['http://dianxinzengzhi/']

    def parse(self, response):
        pass
