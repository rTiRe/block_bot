from typing import Any, Callable, Dict, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from aiogram.enums import ChatMemberStatus

from src.keyboards.follow_channel_keyboard import follow_channel_keyboard
from src.config import settings


class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        user = data['event_from_user']
        is_member = (
            await event.bot.get_chat_member(str(settings.CHANNEL_ID), user.id)
        ).status not in (
            ChatMemberStatus.KICKED,
            ChatMemberStatus.LEFT,
            ChatMemberStatus.RESTRICTED,
        )
        if is_member:
            return await handler(event, data)
        print(type(event))
        if isinstance(event, CallbackQuery):
            await event.answer()
        if isinstance(event, Message):
            await event.delete()
        await event.bot.send_message(
            user.id,
            text='Для работы бота необходима подписка на канал!',
            reply_markup=follow_channel_keyboard,
        )
        return