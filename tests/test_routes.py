from fastapi.testclient import TestClient
from fastapi import status

from app.main import app
import pytest

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['status'] == "API is running!"
    
