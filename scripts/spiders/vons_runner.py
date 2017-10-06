import scrapy
from scrapy.crawler import CrawlerProcess

class VonsSpider(scrapy.Spider):
    name = "vons"

    custom_settings = {
        'CONCURRENT_REQUESTS': '1',
        'DOWNLOAD_DELAY': 3
    }

    def start_requests(self):
        f = open('vonsurl', 'r') # file containing url of weekly ad
        file_url = f.readline() 
        f.close()

        file_url += '/Weekly/2/3' # jump past special ad pages w/ inconsistent html
        urls = [file_url]
        """
        
        urls = [
            'http://vons.safeway.com/Circular/Pasadena-2355-East-Colorado-Blvd/6A1275112/Weekly/2/3'
        ]
        """
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

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


#process = CrawlerProcess({
#        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#})
##
##def start_spider():
#process.crawl(VonsSpider)
#process.start() # the script will block here until the crawling is finished
