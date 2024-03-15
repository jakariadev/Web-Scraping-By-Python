import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllProductsSpider(CrawlSpider):
    name = "all_products"
    allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com"]
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://books.toscrape.com', headers={
            'User-Agent': self.user_agent
        })

    rules = (Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback="parse_item", follow=True),)

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath('//h1/text()').get(),
            'price': response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').get()
        }
