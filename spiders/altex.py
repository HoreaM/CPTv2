import requests
from bs4 import BeautifulSoup
from datetime import datetime
from spiders.base_spider import BaseSpider


class Altex(BaseSpider):
    name = 'altex.ro'

    def __init__(self, start_time):
        self.start_time = start_time

    def start_scraping(self, link, product_name):
        result = requests.get(link)
        print(result.status_code)

        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        products = soup.select('.Product')
        prod = {}
        items = []
        for product in products:
            stock = product.select('.Status')[0].get_text().strip()
            if stock != 'Stoc epuizat':
                prod['title'] = product.select('.js-ProductClickListener')[0].get_text().strip()
                prod['link'] = product.select('.js-ProductClickListener')[0].attrs['href'].strip()
                prod['price'] = product.select('.Price-int')[0].get_text().strip().replace(".", "")
                prod['product-name'] = product_name
                prod['retailer'] = 'altex.ro'
                prod['date'] = str(datetime.now())
                items.append(prod.copy())
        item = min(items, key=lambda x: x.get('price'))
        return item
