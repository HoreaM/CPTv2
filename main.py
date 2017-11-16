import time
from spiders.cel import Cel
from utils.utils import write_json, get_new_deals


def start_spiders():
    new_product_list = []
    start_time = time.strftime("%d.%m.%Y-%H.%M")
    # cel.ro spider
    cel = Cel(start_time)
    new_product_list.extend(cel.start_requests())
    # compare new data with old data
    get_new_deals(new_product_list)
    # write new data
    write_json(start_time, new_product_list)


def main():
    start_spiders()


if __name__ == '__main__':
    main()
