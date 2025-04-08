import logging
from config import CONFIG

def setup_logger():
    log_level = getattr(logging, CONFIG["LOG_LEVEL"], logging.INFO)
    logging.basicConfig(level=log_level,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[logging.StreamHandler()])
    logger = logging.getLogger(__name__)
    return logger

logger = setup_logger()
