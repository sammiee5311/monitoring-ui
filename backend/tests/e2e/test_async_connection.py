import pytest
from fastapi import status
from httpx import AsyncClient
from main import HOST, PORT, app

URL = f"http://{HOST}:{PORT}"


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url=URL) as ac:
        response = await ac.get("/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"message": "It is a backend server."}


@pytest.mark.anyio
async def test_temp_router():
    async with AsyncClient(app=app, base_url=URL) as ac:
        response = await ac.get("/temp/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"message": f"message: `Hello World` from backend."}
