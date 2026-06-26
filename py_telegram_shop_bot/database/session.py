# -*- coding: utf-8 -*-
"""Функции для создания и получения сессии базы данных SQLAlchemy."""

from typing import Final

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker


__session: Session | None = None
base: Final = declarative_base()


def create_session(database_path: str) -> str:
    """Создаёт сессию базы данных SQLAlchemy.

    Args:
        database_path (str): Путь к файлу базы данных.

    Returns:
        str: Адрес (URL) подключения к базе данных.
    """
    global __session

    url: str = f"sqlite:///{database_path}?check_same_thread=False"
    engine: Engine = create_engine(url=url, echo=False)
    __session = sessionmaker(bind=engine)
    base.metadata.create_all(engine)

    return url


def get_session() -> Session | None:
    """Возвращает сессию базы данных SQLAlchemy если она была инициализирована.

    Returns:
        sqlalchemy.orm.Session: Сессия базы данных.
        None: Если сессия не была инициализирована
    """
    return None if __session is None else __session()
