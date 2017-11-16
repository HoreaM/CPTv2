import json
import pkgutil
from abc import ABCMeta, abstractmethod


class BaseSpider(metaclass=ABCMeta):
    name = ''
    start_time = ''

    def start_requests(self):
        product_list = []
        products = json.loads(pkgutil.get_data('resources', 'urls.json').decode())
        for name, urls in products.items():
            for item in urls:
                (retailer, link), = item.items()
                if self.name == retailer:
                    product_list.append(self.start_scraping(link, name))
        return product_list

    @abstractmethod
    def start_scraping(self, link, name):
        pass
