from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import structlog
from fastapi import FastAPI

from choice_paralysis.src.config import settings
from choice_paralysis.src.infrastructure.db import check_db_connection, engine
from choice_paralysis.src.infrastructure.logging import setup_logging

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

setup_logging()
logger: structlog.BoundLogger = structlog.get_logger(__name__)


@asynccontextmanager
async def lifespan() -> AsyncIterator:
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


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)


@app.get("/health")
async def health_check() -> dict[str, str]:
    logger.info("health_check_accessed", some_metric=100)
    return {"status": "active"}
