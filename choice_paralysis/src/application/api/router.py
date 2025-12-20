from fastapi import APIRouter

from choice_paralysis.src.application.api.match.router import router as match_router
from choice_paralysis.src.application.api.system.health import router as health_router

api_router = APIRouter()

api_router.include_router(health_router, tags=["system"])
api_router.include_router(match_router, prefix="/matches", tags=["matches"])
