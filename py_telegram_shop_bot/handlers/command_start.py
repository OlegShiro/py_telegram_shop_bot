from loguru import logger

from database import get_session
from database.models import User


async def command_start(message):
    uid = message.from_user.id
    session = get_session()
    if not session.query(User).filter_by(uid=uid).first():
        session.add(User(uid=uid))
        session.commit()
        logger.info(f"Зарегистрирован новый пользователь: {uid}")
        await message.answer("Регистрация успешна.")
    await message.answer("Привет, это Бот для продажи цифровых товаров в " \
        "Телеграм. В данный момент я нахожусь в разработке.")
