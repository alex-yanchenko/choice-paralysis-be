from uuid import UUID, uuid4

from choice_paralysis.src.domain.match.entities import Match


class MatchProvider:
    """
    Domain Logic Provider.

    Returns Domain Entities (Match), not API schemas.
    """

    async def create_match(self, title: str, platform: str) -> Match:
        # 1. Logic
        # 2. DB Interaction (mocked)
        # 3. Return Entity
        return Match(id=uuid4(), title=title, platform=platform)

    async def get_match(self, match_id: UUID) -> Match | None:
        return Match(id=match_id, title="Domain Match", platform="PS5")
