import logging

def Logger():
    logging.basicConfig(filename="./logs/automation.log",
                        level=logging.INFO,
                        format="%(asctime)s : %(levelname)s : %(message)s",
                        filemode="a",
                        force=True
                        )
    logger= logging.getLogger()
    return logger
