# -*- coding: utf-8 -*-
"""Модель таблицы пользователей базы данных SQL."""

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer

from database.session import base


class User(base):
    """Модель таблицы пользователей базы данных SQL."""
    __tablename__: str = "users"

    # ID пользователя в Telegram
    uid: Column = Column(Integer, autoincrement=True, primary_key=True)

    # Дата и время первого захода пользователя в бота в формате UTC.
    registered_at: Column = Column(DateTime,
                                   default=datetime.now(timezone.utc))
