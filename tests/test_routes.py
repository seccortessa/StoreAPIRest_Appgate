from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

import pytest

client = TestClient(app)

# main test fpr functionality
def test_root():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['status'] == "API is running!"


# tests for invalid/out of range parameters
def test_invalid_product_id():
    response = client.get('/price/', params = {"product_id": 9999, "brand_id": 1, "application_date": "2020-06-15T10:00:00"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Parameter(s) not found: product_id"

def test_invalid_brand_id():
    response = client.get('/price/', params = {"product_id": 35455, "brand_id": 5, "application_date": "2020-06-15T10:00:00"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Parameter(s) not found: brand_id"

def test_invalid_date():
    response = client.get('/price/', params = {"product_id": 35455, "brand_id": 1, "application_date": "2040-06-15T10:00:00"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Entered date out of range"


# set of params and expected responses parametrized for tests
@pytest.mark.parametrize(
    "application_date, product_id, brand_id, expected_status_code, expected_response",
    [
        ("2020-06-14T10:00:00", 35455, 1, status.HTTP_200_OK, {"product_id": 35455,"brand_id": 1, "price_list": 1, "start_date": "2020-06-14T00:00:00", "end_date": "2020-12-31T23:59:59", "price": 32.5}),
        ("2020-06-14T16:00:00", 35455, 1, status.HTTP_200_OK, {"product_id": 35455,"brand_id": 1, "price_list": 2, "start_date": "2020-06-14T15:00:00", "end_date": "2020-06-14T18:30:00", "price": 25.45}),
        ("2020-06-15T10:00:00", 35455, 1, status.HTTP_200_OK, {"product_id": 35455,"brand_id": 1, "price_list": 3, "start_date": "2020-06-15T00:00:00", "end_date": "2020-06-15T11:00:00", "price": 30.5}),
        ("2020-06-15T21:00:00", 35455, 1, status.HTTP_200_OK, {"product_id": 35455,"brand_id": 1, "price_list": 4, "start_date": "2020-06-15T16:00:00", "end_date": "2020-12-31T23:59:59", "price": 38.95})
    ],
)

# perform all the four tests woth the given parameters
def test_specific(application_date, product_id, brand_id, expected_status_code, expected_response):
    response = client.get('/price/', params = {"product_id": product_id, "brand_id": brand_id, "application_date": application_date})
    assert response.status_code == expected_status_code
    assert response.status_code == status.HTTP_200_OK
    if expected_status_code == status.HTTP_200_OK:
        assert response.json() == expected_response