import scrapy
from scrapy.crawler import CrawlerProcess
from vons_runner import VonsSpider
from allrecipes_runner import RecipesSpider

def start_spiders():
    process = CrawlerProcess()
    process.crawl(VonsSpider)
    process.crawl(RecipesSpider)
    process.start()

