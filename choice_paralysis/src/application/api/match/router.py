from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from choice_paralysis.src.application.api.match.schemas import MatchCreateRequest, MatchResponse
from choice_paralysis.src.domain.match.provider import MatchProvider
from choice_paralysis.src.infrastructure.di import get_container

router = APIRouter()


def get_provider() -> MatchProvider:
    return get_container().resolve(MatchProvider)


@router.post("/", response_model=MatchResponse, status_code=status.HTTP_201_CREATED)
async def create_match(
    request: MatchCreateRequest,
    provider: Annotated[MatchProvider, Depends(get_provider)],
) -> MatchResponse:
    # Call Domain
    match_entity = await provider.create_match(
        title=request.title,
        platform=request.platform,
    )

    # Map Domain Entity -> API Response
    return MatchResponse(id=match_entity.id, title=match_entity.title)


@router.get("/{match_id}", response_model=MatchResponse)
async def get_match(
    match_id: UUID,
    provider: Annotated[MatchProvider, Depends(get_provider)],
) -> MatchResponse:
    match_entity = await provider.get_match(match_id)

    if not match_entity:
        raise HTTPException(status_code=404, detail="Match not found")

    return MatchResponse(id=match_entity.id, title=match_entity.title)
