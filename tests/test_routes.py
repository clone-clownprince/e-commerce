import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert "products" in response.json
    assert len(response.json["products"]) > 0

def test_add_to_cart(client):
    # Adjusting method to GET as per your /add-to-cart route
    response = client.get('/add-to-cart')
    assert response.status_code == 200
    assert "message" in response.json
    assert "cart" in response.json
    assert len(response.json["cart"]) > 0

def test_clear_cart(client):
    # Add an item to the cart first
    client.get('/add-to-cart')
    # Then clear the cart
    response = client.get('/clear-cart')
    assert response.status_code == 200
    assert response.json["message"] == "Your cart has been cleared."
