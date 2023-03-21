import logging
from logging.config import fileConfig
from functools import lru_cache

from uvicorn.logging import ColourizedFormatter


UNICORNIFY = "unicornify"


@lru_cache()
def get_logger():
    return logging.getLogger(UNICORNIFY)


def setup_logger():
    # Load logger config
    fileConfig("logger.ini")
    logger = get_logger()

    return logger


class LoggerFormatter(ColourizedFormatter):
    pass
