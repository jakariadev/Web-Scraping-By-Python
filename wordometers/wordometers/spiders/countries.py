import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        countries = response.xpath("//td/a")

        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # yield{
            #     "name": name,
            #     "link": link
            # }

            # to follow link and make request
            # method 1 [absolute url]
            # absolute_url = f"https://www.worldometers.info{link}"
            # yield scrapy.Request(url=absolute_url)

            # method 2 [absolute url]
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url)

            # method 3 [relative url]
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})

    def parse_country(self, response):
        # logging.info(response.name)
        name = response.request.meta.get('country_name')
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed "
                              "table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                "country": name,
                "year": year,
                "population": population
            }
