from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import structlog

from choice_paralysis.src.infrastructure.db import check_db_connection, engine

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from fastapi import FastAPI

logger: structlog.BoundLogger = structlog.get_logger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator:
    logger.info("system_startup", status="warming_up")

    try:
        await check_db_connection()
        logger.info("database_connection_check", status="established")
    except Exception as e:
        logger.exception("startup_failure", error=str(e))

        raise

    yield

    logger.info("system_shutdown")

    await engine.dispose()
