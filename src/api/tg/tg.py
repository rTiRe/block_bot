import asyncio

from aiogram.types import Update
from fastapi.responses import ORJSONResponse
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.config.settings import settings
from src.api.tg.router import router
from bg_tasks import background_tasks
from bot import get_dp, get_bot


@router.post(settings.BOT_WEBHOOK_URL)
async def home_post(
    request: Request,
) -> JSONResponse:
    data = await request.json()
    update = Update(**data)
    dp = get_dp()
    task = asyncio.create_task(dp.feed_webhook_update(get_bot(), update))
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)
    return ORJSONResponse({"message": "Hello"})