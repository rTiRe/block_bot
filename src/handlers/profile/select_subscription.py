from aiogram import F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiocryptopay import AioCryptoPay
from aiocryptopay.const import Assets

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


@router.callback_query(ProfileStates.select_subscription, F.data == 'week')
async def buy_week_subscription(query: CallbackQuery, state: FSMContext, crypto_pay: AioCryptoPay) -> None:
    await query.answer()
    invoice = await crypto_pay.create_invoice(amount=1,  asset=Assets.TON)
    invoice_url = invoice.bot_invoice_url
    await query.message.edit_text(
        text='Оплати',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f'{invoice.amount}{invoice.asset}', url=invoice_url)],
            ]
        )
    )