import requests
from bs4 import BeautifulSoup
from datetime import datetime
from spiders.base_spider import BaseSpider


class Pcgarage(BaseSpider):
    name = 'pcgarage.ro'

    def __init__(self, start_time):
        self.start_time = start_time

    def start_scraping(self, link, product_name):
        result = requests.get(link)
        print(result.status_code)

        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        products = soup.select('.product-box')
        prod = {}
        items = []
        for product in products:
            stock = product.select('.pb-availability')[0].get_text().strip()
            if stock != 'Nu este in stoc':
                prod['title'] = product.select('.pb-name a')[0].get_text().strip()
                prod['link'] = product.select('.pb-name a')[0].attrs['href'].strip()
                prod['price'] = product.select('.price')[0].get_text().strip().replace(".", "")[:-7].upper()
                prod['product-name'] = product_name
                prod['retailer'] = 'pcgarage.ro'
                prod['date'] = str(datetime.now())
                items.append(prod.copy())
        item = min(items, key=lambda x: x.get('price'))
        return item
