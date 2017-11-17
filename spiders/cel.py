import requests
from bs4 import BeautifulSoup
from datetime import datetime
from spiders.base_spider import BaseSpider


class Cel(BaseSpider):
    name = 'cel.ro'

    def __init__(self, start_time):
        self.start_time = start_time

    def start_scraping(self, link, product_name):
        result = requests.get(link)
        #print(result.status_code)

        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        products = soup.select('div.productListing-nume')
        prod = {}
        items = []
        for product in products:
            prod['title'] = product.select('.product_name span')[0].get_text().strip()
            prod['link'] = product.select('.product_name')[0].attrs['href'].strip()
            prod['price'] = product.select('.pret_n b')[0].get_text()
            prod['product-name'] = product_name
            prod['retailer'] = 'cel.ro'
            prod['date'] = str(datetime.now())
            items.append(prod.copy())
        item = min(items, key=lambda x: x.get('price'))
        print(items.__len__())
        print(item['price'])
        return item
