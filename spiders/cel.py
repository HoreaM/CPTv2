import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from spiders.base_spider import BaseSpider


class Cel(BaseSpider):
    name = 'cel.ro'

    def start_scraping(self, link):
        result = requests.get(link)
        print(result.status_code)

        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        products = soup.select('div.productListing-nume')
        prod = {}
        items = []
        for product in products:
            prod['title'] = product.select('.product_name span')[0].get_text().strip()
            prod['link'] = product.select('.product_name')[0].attrs['href'].strip()
            prod['price'] = product.select('.pret_n b')[0].get_text()
            prod['product-name'] = 'gtx1070'
            prod['retailer'] = 'cel.ro'
            prod['date'] = str(datetime.now())
            items.append(prod.copy())
        item = min(items, key=lambda x: x.get('price'))
        with open('/data/mycsvfile.csv', 'w') as f:
            w = csv.DictWriter(f, item.keys())
            w.writeheader()
            w.writerow(item)
