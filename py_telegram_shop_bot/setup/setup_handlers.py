from loguru import logger

import handlers


def setup_handlers(dispatcher):
    dispatcher.message.register(handlers.echo)
    logger.debug("Обработчики настроены.")
