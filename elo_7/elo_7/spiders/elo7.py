import scrapy


class Elo7Spider(scrapy.Spider):
    name = 'elo7'
    allowed_domains = ['elo7.com.br']
    start_urls = ['http://elo7.com.br/']

    def parse(self, response):
        pass
