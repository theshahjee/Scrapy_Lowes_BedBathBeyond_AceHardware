import os
from scrapy.crawler import CrawlerProcess
from acehardware.spiders.ace_spider import AceSpider  # Adjust the import path as needed

def crawl(spider_class, search_query):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'LOG_LEVEL': 'ERROR',  # Optional: Reduce logging verbosity
    })

    process.crawl(spider_class, search_query=search_query)
    process.start()

if __name__ == '__main__':
    search_query = 'Screwdriver'
    crawl(AceSpider, search_query)
