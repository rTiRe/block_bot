from aiogram import F
from aiogram.types import Message

from .router import router
from src.config.settings import SUPPORT_BUTTON


@router.message(F.text == SUPPORT_BUTTON)
async def support(message: Message) -> None:
    await message.answer(
        text='Тех. поддержка - useips.t.me',
    )
    await message.delete()