from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from datetime import datetime
import time

from src.storage.database import get_db
from src.storage.models.user import User, Admin


async def get_user(user_id: int) -> User:
    user = None
    async with get_db() as db:
        statement = select(User).where(User.user_id == user_id)
        result = await db.execute(statement)
        user = result.fetchone()[0]
    return user


async def add_user(user_id: int) -> None:
    async with get_db() as db:
        statement = insert(User).values(user_id=user_id).on_conflict_do_nothing()
        await db.execute(statement)
        await db.commit()


async def add_subscription(user_id: int, subscription_timestamp: int) -> None:
    async with get_db() as db:
        statement = update(
            User,
        ).where(
            User.user_id == user_id,
        ).values(
            subscription=subscription_timestamp,
        )
        await db.execute(statement)
        await db.commit()


async def check_subscription(user_id: int) -> str | bool:
    user = await get_user(user_id)
    if user and user.subscription:
        now = datetime.fromtimestamp(time.time())
        subscription_end = datetime.fromtimestamp(user.subscription / 1000)
        delta = subscription_end - now
        if delta.total_seconds() > 0:
            hours = delta.seconds // 3600
            minutes = (delta.seconds // 60) % 60
            seconds = delta.seconds - hours * 3600 - minutes * 60
            return f'{delta.days} д. {hours} ч. {minutes} м. {seconds} с.'
    return False


async def check_admin(user_id: int) -> bool:
    async with get_db() as db:
        statement = select(Admin).where(Admin.user_id == user_id)
        result = await db.execute(statement)
        if result:
            return True
        return False


async def add_admin(user_id: int) -> None:
    async with get_db() as db:
        statement = insert(Admin).values(user_id=user_id)
        await db.execute(statement)
        await db.commit()
