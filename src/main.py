from aiogram import Dispatcher, Bot
import asyncio
import logging

from config import get_settings


async def main():
    settings = get_settings()

    dp = Dispatcher()

    bot = Bot(
        token=settings.telegram.token.get_secret_value(),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
