import pytest
from httpx import AsyncClient
from src.main import app

@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        yield client