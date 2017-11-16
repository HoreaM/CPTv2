from bin.utils import write_json
from spiders.cel import Cel
import time


class Main:
    product_list = []

    def spiders(self):
        start_time = time.strftime("%d.%m.%Y-%H.%M")
        cel = Cel(start_time)
        self.product_list.extend(cel.start_requests())
        write_json(start_time, self.product_list)


def main():
    start = Main()
    start.spiders()


if __name__ == '__main__':
    main()
