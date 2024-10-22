from fastapi import FastAPI
import asyncio
import logging
import uvicorn

from aiogram import Bot, Dispatcher
from aiocryptopay import AioCryptoPay, Networks
from aiocryptopay.models.update import Update


from src.config.settings import settings
from src.handlers.router import router
from src.middlewares.check_channel import CheckSubscriptionMiddleware
from bg_tasks import background_tasks
from bot import setup_bot, setup_dp
from src.api.tg.router import router as tg_router

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
crypto_pay = AioCryptoPay(token=settings.CRYPTO_PAY_TOKEN, network=Networks.TEST_NET)
dp = Dispatcher()


@crypto_pay.pay_handler()
async def invoice_paid(update: Update, app) -> None:
    print(update)


async def close_session(app) -> None:
    await crypto_pay.close()


async def lifespan(app: FastAPI) -> None: # type: ignore
    dp = Dispatcher()
    setup_dp(dp)
    bot = Bot(token=settings.BOT_TOKEN)
    setup_bot(bot)
    temp = await bot.get_webhook_info()
    await bot.set_webhook(f'{settings.WEBHOOK_URL}{settings.BOT_WEBHOOK_URL}')
    yield
    while background_tasks:
        await asyncio.sleep(0)


def create_app() -> FastAPI:
    app = FastAPI(docs_url='/swagger', lifespan=lifespan)
    app.include_router(tg_router, prefix='/tg', tags=['tg'])
    return app


async def main() -> None:
    dp.include_router(router)
    dp.message.outer_middleware(CheckSubscriptionMiddleware())
    dp.callback_query.outer_middleware(CheckSubscriptionMiddleware())
    dp.workflow_data.update(crypto_pay=crypto_pay)
    await dp.start_polling(bot)


if __name__ == '__main__':
    uvicorn.run('app:create_app', factory=True, host='0.0.0.0', port=80, workers=1)
