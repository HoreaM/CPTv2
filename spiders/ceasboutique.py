import requests
from bs4 import BeautifulSoup
from datetime import datetime
from spiders.base_spider import BaseSpider


class Ceasboutique(BaseSpider):
    name = 'ceasboutique.ro'

    def __init__(self, start_time):
        self.start_time = start_time

    def start_scraping(self, link, product_name):
        result = requests.get(link)
        print(result.status_code)

        c = result.content
        soup = BeautifulSoup(c, 'lxml')
        prod = {}
        alert = False
        if product_name.split(' ', 1)[0] == "Stock":
            alert = True
            product_name = product_name.split(' ', 1)[1]
        prod['title'] = soup.select('#mer-update .box .entry-title')[0].get_text().strip()
        prod['link'] = link
        if soup.select('#mer-update .box ins .amount'):
            prod['price'] = str(soup.select('#mer-update .box ins .amount')[0].contents[0]).replace(u"\u00A0", "")
        else:
            prod['price'] = str(soup.select('#mer-update .box .amount')[0].contents[0]).replace(u"\u00A0", "")
        prod['product-name'] = product_name
        prod['retailer'] = 'ceasboutique.ro'
        prod['date'] = str(datetime.now())
        stock = soup.select('#mer-update .box .out-of-stock')
        if not stock and alert:
            prod['alert'] = True
        return prod
