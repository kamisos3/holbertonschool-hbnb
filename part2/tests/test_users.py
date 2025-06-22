import pytest
import sys
import os
from app import create_app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_create_user_success(client):
    response = client.post('/api/v1/users/', json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201

def test_create_user_invalid_email(client):
    response = client.post('/api/v1/users/', json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "bademail"
    })
    assert response.status_code == 400

def test_create_user_missing_fields(client):
    respone = client.post('/api/v1/users/', json={
        "first_name": "",
        "last_name": "",
        "email": ""
    })
    assert response.status_code == 400
