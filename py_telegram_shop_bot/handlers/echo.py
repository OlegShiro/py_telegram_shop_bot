from loguru import logger


async def echo(message):
    logger.debug("ECHO.")
    await message.answer(message.text)
