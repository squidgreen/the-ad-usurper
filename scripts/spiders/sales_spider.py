import scrapy


class SalesSpider(scrapy.Spider):
    name = "sales"

    custom_settings = {
        'CONCURRENT_REQUESTS': '1',
        'DOWNLOAD_DELAY': 0.25
    }

    start_urls = [
        'http://vons.safeway.com/Circular/Pasadena-2355-East-Colorado-Blvd/6A1275112/Weekly/2/3'
    ]

    def parse(self, response):
        for food in response.css('div.tooltip div.rightContent'):
            yield {
                'item': food.css('p.itemTitle::text').extract_first(),
                'price': food.css('p.itemPrice::text').extract_first(),
            }

            # The very last element is the Next Page link
            try: 
                next_page = response.css('div.paging a::attr(href)').extract()[-1]
            except IndexError:
                next_page = None

            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
