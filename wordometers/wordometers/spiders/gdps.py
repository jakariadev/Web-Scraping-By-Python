import scrapy

class GdpsSpider(scrapy.Spider):
    name = "gdps"
    allowed_domains = ["worldpopulationreview.com"]
    start_urls = ["https://worldpopulationreview.com/country-rankings/countries-by-national-debt/"]

    def parse(self, response):
        rows = response.xpath('(//div[@class="m-0 overflow-auto p-0 max-h-[60vh]"])[1]/table/tbody/tr')
        for row in rows:
            name = row.xpath(".//td[1]/span/a/text()").get()
            gdp = row.xpath(".//td[2]/span/text()").get()
            yield {
                "country": name,
                "gdp": gdp
            }
