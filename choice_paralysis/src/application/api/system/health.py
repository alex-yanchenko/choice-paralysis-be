from typing import Literal

import structlog
from fastapi import APIRouter
from pydantic import BaseModel

logger: structlog.BoundLogger = structlog.get_logger(__name__)

router = APIRouter()


class HealthCheckResponse(BaseModel):
    status: Literal["active"]


@router.get("/health")
async def health_check() -> HealthCheckResponse:
    logger.info("health_check_accessed", some_metric=100)
    return HealthCheckResponse(status="active")
