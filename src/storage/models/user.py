from sqlalchemy import Integer, UUID
from sqlalchemy.orm import Mapped, mapped_column
import uuid

from .meta import Base

class UUIDMixin:
    id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        unique=True,
        primary_key=True,
        default=uuid.uuid4,
    )


class User(Base, UUIDMixin):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    subscription: Mapped[int] = mapped_column(Integer, index=True, nullable=True, default=None)


class Admin(Base, UUIDMixin):
    __tablename__ = 'admins'
    user_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)