# -*- coding: utf-8 -*-
"""Настройка конфигурации бота."""

from configparser import ConfigParser

import config


def setup_config(config_path: str) -> None:
    """Читает и обрабатывает файл конфигурации бота."""
    raw_config: ConfigParser = ConfigParser()
    raw_config.read(filenames=config_path)

    # Конфигурация бота
    config_bot: tuple = raw_config["BOT"]
    config.BOT_TOKEN = config_bot["token"]

    # Конфигурация логирования
    config_logger: tuple = raw_config["LOGGING"]
    config.LOG_FORMAT = config_logger["format"]
    config.LOG_PATH = config_logger["log_path"]
    config.LOG_LEVEL_FILE = config_logger["level_file"]
    config.LOG_LEVEL_OUTPUT = config_logger["level_output"]

    print("Файл конфигурации загружен.")  # "Логирование"
