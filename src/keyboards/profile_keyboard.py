from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.config import settings


async def profile_keyboard(subscription: bool) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Наш канал', url=settings.CHANNEL_URL)
    if not subscription:
        builder.button(text='Купить подписку', callback_data='buy_sub')
    builder.adjust(1, 1)
    return builder.as_markup()
