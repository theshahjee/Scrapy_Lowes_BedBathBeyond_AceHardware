import scrapy
import json
from lowes_scraper.items import Refrigerator  # Ensure you have this defined in items.py

class RefrigeratorSpider(scrapy.Spider):
    name = 'refrigerator'
    start_urls = ['https://www.lowes.com']
    
    custom_headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.lowes.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
    }



    def parse(self, response):
        # Navigate to the refrigerator category
        url = "https://www.lowes.com/c/Refrigerators-Appliances"
        yield scrapy.Request(url, callback=self.parse_category)

    def parse_category(self, response):
        # Extract category links (you may need to adjust the selectors based on the website structure)
        categories = response.css('div.imagecolumncontainer div.grid-100 div.grid-16 a::attr(href)').getall()
        for category in categories:
            yield scrapy.Request(f"https://www.lowes.com{category}", callback=self.parse_refrigerators)

    def parse_refrigerators(self, response):
        # Extract links to individual refrigerator products
        refrigerators = response.xpath("//div[@aria-label='product details']/a/@href").getall()
        for refrigerator in refrigerators:
            yield scrapy.Request(f"https://www.lowes.com{refrigerator}", callback=self.parse_refrigerator)

        # Follow pagination links
        next_page = response.xpath("//link[@rel='next']/@href").get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse_refrigerators)

    def parse_refrigerator(self, response):
        # Extract product details
        if '/collections/' not in response.url:
            brand = response.css('span.brand::text').get()
            refrigerator_json = json.loads(response.xpath("//script[@type='application/ld+json']/text()").get())
            category = str(refrigerator_json[1]["itemListElement"][2]["name"])
            title = str(refrigerator_json[2]["name"])
            sku = response.url.split('/')[-1]
            url = response.url

            # Create a Refrigerator item
            refrigerator = Refrigerator(title=title, brand=brand, category=category, url=url, sku=sku)
            yield refrigerator
