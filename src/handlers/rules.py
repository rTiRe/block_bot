from aiogram import F
from aiogram.types import Message

from .router import router
from src.config.settings import RULES_BUTTON

@router.message(F.text == RULES_BUTTON)
async def rules(message: Message) -> None:
    await message.answer(
        text='Правила',
    )
    await message.delete()