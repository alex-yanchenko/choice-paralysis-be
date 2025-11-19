from datetime import datetime

from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ModelBase(AsyncAttrs, DeclarativeBase):
    pass


class TimestempMixin:
    created_at: Mapped[datetime] = mapped_column(
        service_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        service_default=func.now(), onupdate=func.now(), nullable=False
    )
