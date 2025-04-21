import logging

def setup_logger(name: str, level=logging.INFO):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
