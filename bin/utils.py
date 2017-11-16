import json
import os.path


def write_json(filename, product_list):
    with open(os.path.dirname(__file__) + '/../data/' + filename + '.json', 'a') as fp:
        json.dump(product_list, fp, indent=2)
