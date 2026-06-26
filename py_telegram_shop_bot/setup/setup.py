# -*- config: utf-8 -*-
"""Настраивает бота при его запуске."""

from aiogram import Bot, Dispatcher
from loguru import logger

from database import create_session
from .setup_config import setup_config
from .setup_logger import setup_logger
from .setup_bot import setup_bot
from .setup_handlers import setup_handlers


def setup() -> tuple[Bot, Dispatcher]:
    """Настраивает бота при его запуске согласно файла конфигурации.

    Returns:
        tuple[Bot, Dispatcher]: Объекты бота и диспетчера aiogram.
    """
    setup_config(config_path="config.ini")
    setup_logger()
    create_session(database_path="database/database.db")
    bot, dispatcher = setup_bot()
    setup_handlers(dispatcher)

    logger.debug("Настройки бота применены успешно.")  # Логирование
    logger.info("Запуск бота.")  # Логирование

    return bot, dispatcher
