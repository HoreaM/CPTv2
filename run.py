import time

from spiders.altex import Altex
from spiders.ceasboutique import Ceasboutique
from spiders.cel import Cel
from spiders.emag import Emag
from spiders.pcgarage import Pcgarage
from utils.utils import write_json, get_new_deals


def start_spiders():
    new_product_list = []
    start_time = time.strftime("%d.%m.%Y-%H.%M")

    # cel.ro spider
    cel = Cel(start_time)
    new_product_list.extend(cel.start_requests())

    # emag.ro spider
    emag = Emag(start_time)
    new_product_list.extend(emag.start_requests())

    # pcgarage.ro spider
    pcgarage = Pcgarage(start_time)
    #new_product_list.extend(pcgarage.start_requests())

    # altex.ro spider
    altex = Altex(start_time)
    #new_product_list.extend(altex.start_requests())

    # ceasboutique.ro spider
    ceasboutique = Ceasboutique(start_time)
    #new_product_list.extend(ceasboutique.start_requests())

    # compare new data with old data
    get_new_deals(new_product_list)
    # write new data
    if new_product_list:
        write_json(start_time, new_product_list)


def main():
    start_spiders()


if __name__ == '__main__':
    main()
