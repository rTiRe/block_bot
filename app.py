import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.config.settings import settings
from src.handlers.router import router

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
