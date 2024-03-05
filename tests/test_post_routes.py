from fastapi.testclient import TestClient
import pytest
from main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_get_post_valid(client):
    response = client.get("/posts?author=ali")
    assert response.status_code == 200
    assert len(response.json()) == 1  # 
    post_data = response.json()[0]  
    assert post_data == {
            "id": 3,
            "title": "Post 100",
            "content": "Post1000 by ali",
            "category": "Non existing",
            "author__username": "ali"
        }

def test_get_post_invalid(client):
    response = client.get("/posts?author=noone")
    assert response.status_code == 200  
    assert len(response.json()) == 0  
    print("Test 'test_get_invalid_post' passed.")
