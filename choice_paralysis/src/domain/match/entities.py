from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Match(BaseModel):
    """
    The Domain Entity.
    This represents a Match in our business logic, decoupled from API or DB.
    """

    id: UUID
    title: str
    platform: str

    model_config = ConfigDict(from_attributes=True)
