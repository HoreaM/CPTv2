from spiders.cel import Cel


def start_spiders():
    cel = Cel()
    cel.start_requests()


def main():
    start_spiders()


if __name__ == '__main__':
    main()
