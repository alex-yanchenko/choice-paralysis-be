import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from choice_paralysis.src.main import app


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as c:
        yield c
