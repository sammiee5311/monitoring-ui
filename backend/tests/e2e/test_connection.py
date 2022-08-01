from fastapi import status
from fastapi.testclient import TestClient
from db.sql_alchemy import SqlAlchemyDB
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
