# -*- config: utf-8 -*-
"""Настройка бота при его запуске."""

from loguru import logger

from bot import set_bot, set_dispatcher
from database import create_session
from .setup_config import setup_config
from .setup_logger import setup_logger
from .setup_bot import setup_bot


def setup() -> None:
    """Настраивает бота при его запуске согласно файла конфигурации."""
    setup_config(config_path="config.ini")
    setup_logger()
    create_session(database_path="database/database.db")

    bot, dispatcher = setup_bot()
    set_bot(bot=bot)
    set_dispatcher(dispatcher=dispatcher)

    # Импорт необходим после инициалиации диспетчера, чтобы сработал
    # скрипт "handlers.__init__.py", который выполнит каждый скрипт
    # с обработчиками бота , регистрируя их в диспетчере
    import handlers  # noqa: F401
    logger.debug("Обработчики зарегистрированы.")  # Логирование

    logger.debug("Настройки бота применены успешно.")  # Логирование
    logger.info("Запуск бота.")  # Логирование
