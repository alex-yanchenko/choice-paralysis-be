# ruff: noqa: E402
from choice_paralysis.src.infrastructure.logging import setup_logging

setup_logging()

from fastapi import FastAPI

from choice_paralysis.src.application.api.middleware import lifespan
from choice_paralysis.src.application.api.router import api_router
from choice_paralysis.src.config import settings

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

app.include_router(api_router)
