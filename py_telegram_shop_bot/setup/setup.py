# -*- config: utf-8 -*-
"""Настройка бота при его запуске."""

from loguru import logger

from bot import set_bot, set_dispatcher
from database import create_session
from .setup_config import setup_config
from .setup_logger import setup_logger
from .setup_bot import setup_bot
from .setup_handlers import setup_handlers


def setup() -> None:
    """Настраивает бота при его запуске согласно файла конфигурации."""
    setup_config(config_path="config.ini")
    setup_logger()
    create_session(database_path="database/database.db")

    bot, dispatcher = setup_bot()
    set_bot(bot=bot)
    set_dispatcher(dispatcher=dispatcher)
    
    setup_handlers(dispatcher=dispatcher)

    logger.debug("Настройки бота применены успешно.")  # Логирование
    logger.info("Запуск бота.")  # Логирование
