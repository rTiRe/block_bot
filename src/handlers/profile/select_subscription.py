from aiogram import F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from .router import router
from src.states import ProfileStates
from src.keyboards.subscription_select_keyboard import subscription_select_keyboard


@router.callback_query(ProfileStates.show_profile, F.data == 'buy_sub')
async def select_subscription(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()
    await state.set_state(ProfileStates.select_subscription)
    await query.message.edit_text(
        text='Выберите тип подписки:',
        reply_markup=subscription_select_keyboard,
    )
    await query.message.answer_invoice()