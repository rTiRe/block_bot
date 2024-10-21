from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from src.config import settings

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=settings.START_DEMOLITION_BUTTON),
        ],
        [
            KeyboardButton(text=settings.PROFILE_BUTTON),
            KeyboardButton(text=settings.SUPPORT_BUTTON),
        ],
        [
            KeyboardButton(text=settings.RULES_BUTTON),
        ],
    ],
    resize_keyboard=True,
)