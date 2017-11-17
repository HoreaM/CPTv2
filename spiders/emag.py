import requests
from bs4 import BeautifulSoup
from datetime import datetime
from spiders.base_spider import BaseSpider


class Emag(BaseSpider):
    name = 'emag.ro'

    def __init__(self, start_time):
        self.start_time = start_time

    def start_scraping(self, link, product_name):
        result = requests.get(link)
        print(result.status_code)

        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        products = soup.select('.js-products-container .js-product-data')
        prod = {}
        items = []
        for product in products:
            stock = product.select('.product-stock-status')[0].get_text().strip()
            if stock != 'stoc epuizat':
                prod['title'] = product.select('.product-title')[0].get_text().strip().replace("\u00ae", "")
                prod['link'] = product.select('.product-title')[0].attrs['href'].strip()
                prod['price'] = str(product.select('.product-new-price')[0].contents[0]).replace(".", "")
                prod['product-name'] = product_name
                prod['retailer'] = 'emag.ro'
                prod['date'] = str(datetime.now())
                items.append(prod.copy())
        item = min(items, key=lambda x: x.get('price'))
        return item
