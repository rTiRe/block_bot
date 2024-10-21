from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from .router import router
from src.config import settings
from src.states import ProfileStates
from src.storage.user_utils import check_subscription
from src.keyboards.profile_keyboard import profile_keyboard


@router.message(F.text == settings.PROFILE_BUTTON)
async def profile(message: Message, state: FSMContext) -> None:
    await state.set_state(ProfileStates.show_profile)
    header = '<b>Ваш профиль</b>\n\n'
    name = f'Имя: {message.from_user.first_name}\n'
    username = f'| @{message.from_user.username}' if message.from_user.username else ''
    data = f'Данные: {message.from_user.id} {username}\n'
    subscription = await check_subscription(message.from_user.id)
    remaining_time = f'Подписка: {subscription or "Нет"}'
    response_text = f'{header}{name}{data}{remaining_time}'
    await message.answer(
        text=response_text,
        parse_mode=ParseMode.HTML,
        reply_markup=await profile_keyboard(subscription),
    )
    await message.delete()