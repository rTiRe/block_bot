import asyncio
import logging

from aiogram import Bot, Dispatcher

from config.settings import settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
