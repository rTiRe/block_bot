from aiogram.filters import CommandObject, CommandStart
from aiogram.types import Message

from router import router
from src.keyboards import main_menu


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        'Привет! Я бот для помощи в сносе телеграм групп.',
        reply_markup=main_menu,
    )