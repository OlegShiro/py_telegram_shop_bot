from .setup_config import setup_config
from .setup_logger import setup_logger
from .setup_bot import setup_bot
from .setup_handlers import setup_handlers


def setup():
    global bot, dispatcher

    print("Запуск бота...")
    setup_config()
    setup_logger()

    bot, dispatcher = setup_bot()

    setup_handlers(dispatcher)

    return bot, dispatcher
