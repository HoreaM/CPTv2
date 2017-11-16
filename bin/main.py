import time

from spiders.cel import Cel
from utils.utils import write_json


def start_spiders():
    product_list = []
    start_time = time.strftime("%d.%m.%Y-%H.%M")
    # cel.ro spider
    cel = Cel(start_time)
    product_list.extend(cel.start_requests())


    write_json(start_time, product_list)


def main():
    start_spiders()


if __name__ == '__main__':
    main()
