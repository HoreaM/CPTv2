import json
import os.path
import glob


def write_json(filename, product_list):
    with open(os.path.dirname(__file__) + '/../data/' + filename + '.json', 'a') as json_file:
        json.dump(product_list, json_file, indent=2)


def read_json(filename):
    with open(os.path.dirname(__file__) + '/../data/' + filename + '.json', 'r') as json_file:
        product_list = json.load(json_file)
    return product_list


def last_file():
    list_of_files = glob.glob(os.path.dirname(__file__) + '/../data/*.json')
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)


def get_best_deal(previous_deals, latest_deals):
    best_so_far = min(previous_deals, key=lambda x: x.get('price'))
    best_from_last = min(latest_deals, key=lambda x: x.get('price'))
    if best_from_last.get('price') < best_so_far.get('price'):
        return best_from_last
    else:
        return best_so_far
