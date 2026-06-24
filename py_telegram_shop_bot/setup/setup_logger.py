import sys

from loguru import logger

import config


def setup_logger():
    logger.remove()
    logger.add(sys.stdout, level=config.LOG_LEVEL_OUTPUT,
               format=config.LOG_FORMAT)
    if config.LOG_PATH:
        logger.add(config.LOG_PATH, level=config.LOG_LEVEL_FILE,
                   format=config.LOG_FORMAT)
    logger.debug("Логирование настроено.")
