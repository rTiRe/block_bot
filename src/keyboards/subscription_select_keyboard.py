from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

subscription_select_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='1 неделя', callback_data='week')],
    ]
)