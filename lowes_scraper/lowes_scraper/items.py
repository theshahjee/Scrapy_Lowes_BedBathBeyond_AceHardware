import scrapy

class Refrigerator(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
    sku = scrapy.Field()
