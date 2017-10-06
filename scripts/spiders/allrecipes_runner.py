import scrapy
from scrapy.crawler import CrawlerProcess

class RecipesSpider(scrapy.Spider):
    name = "allrecipes"

    custom_settings = {
        'CONCURRENT_REQUESTS': '1',
        'DOWNLOAD_DELAY': 3
    }

    def start_requests(self):
        f = open('allrecipes_url', 'r') # file containing url of recipe
        file_url = f.readline()
        print("\n\n\n ### string to read recipe from: " + file_url + "\n\n")
        f.close()

        urls = [file_url]
        """
        urls = [
            'http://allrecipes.com/recipe/56352/garlic-prime-rib/?clickId=right%20rail%200&internalSource=rr_feed_recipe&referringId=56352&referringContentType=recipe'
        ]
        """
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for item in response.css('.added::text').extract():
            yield {
                'ingredient': item,
            }

#process = CrawlerProcess({
#        'USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
##'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#})


#def start_recipe_spider():
    #process.crawl(RecipesSpider)
    #process.start()
    #process.stop()
