import logging


def main():
    logging.info("Hello World")
if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        main()
    except (ValueError, KeyError) as err:
        logging.error(err)
    except:
        logging.exception("Internal error")
