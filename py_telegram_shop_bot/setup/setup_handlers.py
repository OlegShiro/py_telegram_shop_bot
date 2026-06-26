from aiogram.filters import Command
from loguru import logger

import handlers


def setup_handlers(dispatcher):
    dispatcher.message.register(handlers.command_start,
                                Command(commands=["start"]))
    logger.debug("Обработчики настроены.")
