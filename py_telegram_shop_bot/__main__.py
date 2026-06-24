# -*- coding: utf-8 -*-
"""
Python Telegram Shop Bot
ID: Project_00106261d

Простой телеграм бот на Python 3 с реализацией функционала интернет-магазина
цифровых товаров и возможностью оплаты через различные платёжные сервисы.
"""

import asyncio

from setup import setup


async def main():
    bot, dispatcher = setup()
    await dispatcher.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
