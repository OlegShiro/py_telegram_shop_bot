# -*- coding: utf-8 -*-
"""Настройка логирования бота."""

import sys

from loguru import logger

import config


def setup_logger() -> None:
    """Настраивает логирование бота согласно файла конфигурации."""
    logger.remove()

    # Вывод в терминал
    logger.add(sink=sys.stdout, level=config.LOG_LEVEL_OUTPUT,
               format=config.LOG_FORMAT)

    # Запись в файл, если в файле конфигурации указан путь
    if config.LOG_PATH:
        logger.add(sink=config.LOG_PATH, level=config.LOG_LEVEL_FILE,
                   format=config.LOG_FORMAT)

    logger.debug("Логирование настроено.")  # Логирование
