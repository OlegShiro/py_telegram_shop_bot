# -*- coding: utf-8 -*-
"""Настройка обработчики бота."""

from aiogram.filters import Command
from aiogram import Dispatcher
from loguru import logger

import handlers


def setup_handlers(dispatcher: Dispatcher) -> None:
    """Настраивает обработчики бота.

    Args:
        dispatcher (Dispatcher): Объект диспетчера бота.
    """
    # Команда '/start'
    dispatcher.message.register(handlers.command_start,
                                Command(commands=["start"]))

    logger.debug("Обработчики настроены.")  # Логирование
