import pytest
from fastapi import status
from httpx import AsyncClient

from sqlalchemy.orm import Session
from db.sql_alchemy import SqlAlchemyDB
from typing import Callable

from routers.grafana import get_db
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


@pytest.mark.anyio
async def test_grafana_router(sqlite_session_factory: Callable[[], Session]):
    async with AsyncClient(app=app, base_url=URL) as ac:

        def overide_get_db() -> SqlAlchemyDB:
            db = SqlAlchemyDB(sqlite_session_factory)
            return db

        app.dependency_overrides[get_db] = overide_get_db

        response = await ac.get("/grafana/?server=test")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.json() == {"error": "test does not contain in grafana servers."}
