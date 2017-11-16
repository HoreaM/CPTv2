import json
import pkgutil
from abc import ABCMeta, abstractmethod


class BaseSpider(metaclass=ABCMeta):
    name = ''

    def start_requests(self):
        products = json.loads(pkgutil.get_data('resources', 'urls.json').decode())
        for name, urls in products.items():
            for item in urls:
                (retailer, link), = item.items()
                if self.name == retailer:
                    self.start_scraping(link)

    @abstractmethod
    def start_scraping(self, link):
        pass
