from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Todo API"}

def test_create_and_get_todo():
    todo = {"id": 1, "task": "Belajar uv & ruff", "done": False}
    response = client.post("/todos", json=todo)
    assert response.status_code == 200

    response = client.get("/todos")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["task"] == "Belajar uv & ruff"
