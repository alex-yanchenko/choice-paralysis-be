import pytest

from choice_paralysis.src.domain.match.provider import MatchProvider


@pytest.mark.asyncio
async def test_create_match():
    provider = MatchProvider()
    match = await provider.create_match(title="Elden Ring", platform="PC")

    assert match.title == "Elden Ring"
    assert match.platform == "PC"
    assert match.id is not None
