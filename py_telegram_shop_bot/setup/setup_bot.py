from aiogram import Bot, Dispatcher
from loguru import logger

import config


def setup_bot():
    bot = Bot(config.BOT_TOKEN)
    dispatcher = Dispatcher()

    logger.debug("Объекты бота и диспетчера настроены.")

    return bot, dispatcher
