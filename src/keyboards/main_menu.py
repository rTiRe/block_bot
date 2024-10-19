from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Начать снос')],
        [KeyboardButton(text='Профиль'), KeyboardButton(text='Тех. Поддержка')],
        [KeyboardButton(text='Правила')],
        [KeyboardButton(text='Наш канал')]
    ],
    resize_keyboard=True,
)