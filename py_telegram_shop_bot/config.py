# -*- coding: utf-8 -*-
"""
Файл конфигурации бота.

Указаны значения по умолчанию. Перезаписываются при запуске
бота данными из файла 'config.ini'.
"""

BOT_TOKEN: str = ""

LOG_FORMAT: str = "<green>{time: HH:mm:ss}</green> | {level: <8} | {message}"
LOG_PATH: str = ""
LOG_LEVEL_FILE: str = "INFO"
LOG_LEVEL_OUTPUT: str = "DEBUG"
