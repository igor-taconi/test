from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import Elo7Item


class Elo7Spider(CrawlSpider):
    name = 'elo7'
    allowed_domains = ['elo7.com.br']
    start_urls = ['http://elo7.com.br/']

    rules = (
        Rule(
            LinkExtractor(restrict_css=('nav a.link'))  # ir a cada categoria
        ),
        Rule(
            LinkExtractor(restrict_css=('.category'))  # ir a cada subcategoria
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths=('//a[@class="btn btn-yellow"]')
            )  # próxima págiina
        ),
        Rule(
            LinkExtractor(restrict_css=('.img-link')),  # acessar cada produto
            callback='parse_product',
        ),
    )

    def parse_product(self, response):
        items = Elo7Item()

        name = response.xpath('//h1[@itemprop="name"]//text()').get()
        price = response.xpath('//span[@itemprop="price"]//text()').get()
        details = ' '.join(
            ''.join(
                response.xpath(
                    '//div[@class="content details"]//li//text()'
                ).getall()
            ).split()
        )
        category = response.css('a.category::text').get()
        subcategory = response.css('a.category::text').getall()[1]

        items['name'] = name
        items['price'] = price
        items['details'] = details
        items['category'] = category
        items['subcategory'] = subcategory
        items['url'] = response.url

        yield items
