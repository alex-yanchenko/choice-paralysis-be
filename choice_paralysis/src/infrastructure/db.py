from typing import TYPE_CHECKING

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from choice_paralysis.src.config import settings
from choice_paralysis.src.infrastructure.env import Environment

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    echo=settings.ENVIRONMENT == Environment.DEV,
    future=True,
)

AsyncSessionLocal = async_sessionmaker[AsyncSession](
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def check_db_connection() -> None:
    async with engine.begin() as connection:
        await connection.execute(text("SELECT 1"))
