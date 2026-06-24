# -*- coding: utf-8 -*-
"""
Python Telegram Shop Bot
ID: Project_00106261d

Простой телеграм бот на Python 3 с реализацией функционала интернет-магазина
цифровых товаров и возможностью оплаты через различные платёжные сервисы.
"""

import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

import config
import handlers


async def main():
    # Инициализация Бота
    bot = Bot(token=config.BOT_TOKEN)
    dispatcher = Dispatcher()

    # Регистрация обработчика ECHO
    dispatcher.message.register(handlers.echo)

    await dispatcher.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    logger.debug("Начало работы.")
    asyncio.run(main())
