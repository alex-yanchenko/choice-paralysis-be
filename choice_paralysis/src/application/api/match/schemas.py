from uuid import UUID

from pydantic import BaseModel


# API Request Schema
class MatchCreateRequest(BaseModel):
    title: str
    platform: str


# API Response Schema
class MatchResponse(BaseModel):
    id: UUID
    title: str
    # We might expose less or different fields than the Domain Entity
