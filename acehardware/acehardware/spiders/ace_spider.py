import scrapy

class AceSpider(scrapy.Spider):
    name = "ace_spider"

    def __init__(self, search_query='', *args, **kwargs):
        super(AceSpider, self).__init__(*args, **kwargs)
        self.search_query = search_query
        self.start_urls = [f'https://www.acehardware.com/search?query={search_query}']

    def parse(self, response):
        products = response.css('li.col-md-4.col-xs-6.mz-productlist-item')

        for product in products:
            product_name = product.css('div.mz-productlisting-info a.mz-productlisting-title::text').get()
            price = product.css('span.custom-price.mz-price::text').get()
            shipping = product.css('span.mz-productdetail-pickup-instore-today div::text').get()
            product_url = product.css('div.mz-productlisting-info a.mz-productlisting-title::attr(href)').get()

            # Print each product's details
            print({
                'product_name': product_name.strip() if product_name else 'N/A',
                'price': price.strip() if price else 'N/A',
                'shipping': shipping.strip() if shipping else 'N/A',
                'product_url': response.urljoin(product_url) if product_url else 'N/A',
            })
