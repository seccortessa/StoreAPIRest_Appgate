# from fastapi import status
# from tests.config_test import client
# import pytest


# # general tests
# # def test_read_products(client):
# #     response = client.get("/products/")
# #     assert response.status_code == status.HTTP_200_OK
# #     assert response.json() == [{"id": 35455, "name": "Product1"}]

# def test_get_price_valid(client):
#     response = client.get("/prices/?product_id=35455&brand_id=1&application_date=2020-06-15T10:00:00")
#     assert response.status_code == status.HTTP_200_OK
#     data = response.json()
#     assert data["product_id"] == 35455
#     assert data["brand_id"] == 1
#     assert data["price"] == 32.5

# def test_get_price_invalid_product(client):
#     response = client.get("/prices/?product_id=9999&brand_id=1&application_date=2020-06-15T10:00:00")
#     assert response.status_code == status.HTTP_404_NOT_FOUND
#     # assert response.json() == {"detail": "Product with ID 9999 not found"}

# def test_get_price_invalid_brand(client):
#     response = client.get("/prices/?product_id=35455&brand_id=9999&application_date=2020-06-15T10:00:00")
#     assert response.status_code == status.HTTP_404_NOT_FOUND
#     # assert response.json() == {"detail": "Brand with ID 9999 not found"}
    
# def test_get_price_invalid_date(client):
#     response = client.get("/prices/?product_id=35455&brand_id=1&application_date=2019-06-15T10:00:00")
#     assert response.status_code == status.HTTP_404_NOT_FOUND
#     # assert response.json() == {"detail": "No price found for product 35455, brand 1, and date 2019-06-15T10:00:00"}
    
    
# def specific_tests(client):
#     response = client.get('/')
#     assert response.status_code == status.HTTP_200_OK
    