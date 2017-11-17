import json
import os.path
import glob
from pushbullet import Pushbullet

from utils import settings


def write_json(filename, product_list):
    with open(os.path.dirname(__file__) + '/../data/' + filename + '.json', 'w') as json_file:
        json.dump(product_list, json_file, indent=2)


def read_json(filename):
    with open(os.path.dirname(__file__) + '/../data/' + filename + '.json', 'r') as json_file:
        product_list = json.load(json_file)
    return product_list


def last_file():
    list_of_files = glob.glob(os.path.dirname(__file__) + '/../data/*.json')
    if list_of_files:
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file
    return False


def get_best_deal(previous_deals, latest_deals):
    best_so_far = min(previous_deals, key=lambda x: x.get('price'))
    best_from_last = min(latest_deals, key=lambda x: x.get('price'))
    if best_from_last.get('price') < best_so_far.get('price'):
        return best_from_last
    else:
        return best_so_far


def get_new_deals(new_product_list):
    last_list = last_file()
    if last_list is not False:
        with open(last_list, 'r') as json_file:
            old_product_list = json.load(json_file)
        better_deals = []
        for old_product in old_product_list:
            for new_product in new_product_list:
                if new_product['retailer'] == old_product['retailer'] and \
                                new_product['product-name'] == old_product['product-name'] and \
                                new_product['price'] < old_product['price']:
                    better_deals.append(new_product.copy())
                elif 'alert' in new_product:
                    better_deals.append(new_product.copy())
        if better_deals:
            new_deals_alert(better_deals)


def new_deals_alert(better_deals):
    pb = Pushbullet(settings.PUSHBULLET_API)
    for deal in better_deals:
        pb.push_link(deal['product-name'] + ' - ' + deal['price'] + ' - ' + deal['retailer'] +
                     ' - ' + deal['title'], deal['link'])
