from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.config import settings

follow_channel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Наш канал', url=settings.CHANNEL_URL)],
    ]
)