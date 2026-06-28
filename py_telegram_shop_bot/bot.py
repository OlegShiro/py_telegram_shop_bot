# -*- coding: utf-8 -*-
"""Хрянит объекты бота и диспетчера для лёгкого доступа к ним."""

from aiogram import Bot, Dispatcher


__bot: Bot | None = None
__dispatcher: Dispatcher | None = None


def get_bot() -> Bot:
    """Возвращает объект бота.

    Returns:
        Bot: Объект бота.
    """
    return __bot


def get_dispatcher() -> Dispatcher:
    """Возвращает объект диспетчера бота.

    Returns:
        Dispatcher: Объект диспетчера бота.
    """
    return __dispatcher


def set_bot(bot: Bot) -> None:
    """Устанавливает объект бота.

    Args:
        bot (Bot): Объект бота.
    """
    global __bot
    __bot = bot


def set_dispatcher(dispatcher: Dispatcher) -> None:
    """Устанавливает объект диспетчера бота.

    Args:
        dispatcher (Dispatcher): Объект диспетчера бота.
    """
    global __dispatcher
    __dispatcher = dispatcher
