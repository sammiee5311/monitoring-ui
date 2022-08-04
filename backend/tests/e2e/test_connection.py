from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from typing import Callable

from db.sql_alchemy import SqlAlchemyDB
from routers.grafana import get_db
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "It is a backend server."}


def test_temp_router():
    response = client.get("/temp/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": f"message: `Hello World` from backend."}


def test_grafana_router(sqlite_session_factory: Callable[[], Session]):
    def overide_get_db() -> SqlAlchemyDB:
        db = SqlAlchemyDB(sqlite_session_factory)
        return db

    app.dependency_overrides[get_db] = overide_get_db

    response = client.get("/grafana/?server=test")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.json() == {"error": "test does not contain in grafana servers."}
