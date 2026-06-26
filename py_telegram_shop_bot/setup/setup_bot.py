# -*- coding: utf-8 -*-
"""Создание объектов бота и диспетчера aiogram."""

from aiogram import Bot, Dispatcher
from loguru import logger

import config


def setup_bot() -> tuple[Bot, Dispatcher]:
    """Функция создания объектов бота и диспетчера aiogram.

    Returns:
        tuple[Bot, Dispatcher]: Объекты бота и диспетчера aiogram.
    """
    bot: Bot = Bot(token=config.BOT_TOKEN)
    dispatcher: Dispatcher = Dispatcher()

    logger.debug("Объекты бота и диспетчера созданы.")  # Логирование

    return bot, dispatcher
