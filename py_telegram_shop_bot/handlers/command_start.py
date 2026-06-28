# -*- coding: utf-8 -*-
"""
Обработчик команды '/start'.

Добавляет пользователя в базу данных SQL, если он в первый раз зашёл в бота
и выводит приветственное сообщение.
"""

from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger
from sqlalchemy.orm import Session

import text
from bot import get_dispatcher
from database import get_session
from database.models import User


__dispatcher: Dispatcher = get_dispatcher()


@__dispatcher.message(Command("start"))
async def command_start(message: Message) -> None:
    """Обработчик команды '/start'.

    Добавляет пользователя в базу данных SQL, если он в первый раз зашёл в бота
    и выводит приветственное сообщение.
    """
    uid: int = message.from_user.id
    session: Session = get_session()

    # Добавляем пользователя в базу данных, если его там нет
    if not session.query(User).filter_by(uid=uid).first():
        session.add(instance=User(uid=uid))
        session.commit()

        # Логирование
        logger.info(f"Зарегистрирован новый пользователь: {uid}")

    await message.answer(text.COMMAND_START)
