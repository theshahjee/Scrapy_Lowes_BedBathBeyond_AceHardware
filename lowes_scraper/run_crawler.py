from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .lowes_scraper.spiders.refrigerator_spider import RefrigeratorSpider

def crawl(spider):
    process = CrawlerProcess(get_project_settings())
    results = []
    
    def save_item(item):
        results.append(item)

    process.crawl(spider, item_callback=save_item)
    process.start()
    return results

if __name__ == '__main__':
    refrigerator_data = crawl(RefrigeratorSpider)
    print(refrigerator_data)
