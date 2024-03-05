from fastapi.testclient import TestClient
import pytest
from main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_get_user_valid(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {
        "username": "user1",
        "id": 1,
    }
    print("Test 'test_get_valid_user' passed.")

def test_get_users_invalid(client):
    response = client.get("/users/19")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found 404"
    print("Test 'test_get_invalid_user' passed.")
    
