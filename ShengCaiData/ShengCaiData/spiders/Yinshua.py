import scrapy


class YinshuaSpider(scrapy.Spider):
    name = 'Yinshua'
    allowed_domains = ['yinshuafuwu']
    start_urls = ['http://yinshuafuwu/']

    def parse(self, response):
        pass
