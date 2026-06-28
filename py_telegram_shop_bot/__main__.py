# -*- coding: utf-8 -*-
"""
Python Telegram Shop Bot
ID: Project_00106261d
Разработчик: Олег Широ (https://github.com/OlegShiro)
Лицензия: MIT License

Простой телеграм бот на Python 3 с реализацией функционала интернет-магазина
цифровых товаров и возможностью оплаты через различные платёжные сервисы.
"""

import asyncio

from bot import get_bot, get_dispatcher
from setup import setup


async def main() -> None:
    """Запуск бота."""
    setup()
    await get_dispatcher().start_polling(get_bot(), skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main=main())
