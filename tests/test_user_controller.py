import pytest
from app import create_app
from app.infra.db import init_db, SessionLocal
import os

@pytest.fixture
def client(tmp_path, monkeypatch):
    # usar DB en path temporal para pruebas
    db_path = tmp_path / "test.db"
    uri = f"sqlite:///{db_path}"
    from app.config import Config
    class TestConfig(Config):
        SQLALCHEMY_DATABASE_URI = uri
        DEBUG = True

    app = create_app(TestConfig)
    with app.test_client() as c:
        yield c

def test_create_and_get_user(client):
    res = client.post("/users/", json={"username": "carlos", "email": "carlos@example.com"})
    assert res.status_code == 201
    body = res.get_json()
    user_id = body["id"]

    res2 = client.get(f"/users/{user_id}")
    assert res2.status_code == 200
    data = res2.get_json()
    assert data["username"] == "carlos"
