from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

if TYPE_CHECKING:
    from datetime import datetime


class ModelBase(AsyncAttrs, DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        service_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        service_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
