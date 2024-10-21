from aiogram.filters import CommandObject, CommandStart
from aiogram.types import Message
from src.storage.user_utils import add_user

from .router import router
from src.keyboards import main_menu


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        'Привет! Я бот.',
        reply_markup=main_menu,
    )
    await add_user(message.from_user.id)
    await message.delete()