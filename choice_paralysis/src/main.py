from contextlib import asynccontextmanager

import structlog
import uvicorn
from fastapi import FastAPI

from choice_paralysis.src.config import settings
from choice_paralysis.src.infrastructure.db import check_db_connection, engine
from choice_paralysis.src.infrastructure.logging import setup_logging

setup_logging()
logger: structlog.BoundLogger = structlog.get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("system_startup", status="warming_up")

    try:
        await check_db_connection()
        logger.info("database_connection_check", status="established")
    except Exception as e:
        logger.error("startup_failure", error=str(e))
        raise e

    yield

    logger.info("system_shutdown")

    await engine.dispose()


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)


@app.get("/health")
async def health_check():
    logger.info("helth_check_accessed", some_metric=100)
    return {"status": "active"}


def start():
    uvicorn.run(
        "choice_paralysis.src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,  # settings.ENVIRONMENT == Environment.DEV,
    )
