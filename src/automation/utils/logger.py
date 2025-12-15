import logging
from logging.handlers import RotatingFileHandler

LOG_FILE = "logs/activity.log"

def setup_logger():
    logger = logging.getLogger("spike_bot")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=5_000_000, backupCount=3
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
