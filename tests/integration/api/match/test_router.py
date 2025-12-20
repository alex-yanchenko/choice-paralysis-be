import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_match_api(client: AsyncClient):
    response = await client.post(
        "/matches/",
        json={"title": "Zelda", "platform": "Switch"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Zelda"
    assert "id" in data
