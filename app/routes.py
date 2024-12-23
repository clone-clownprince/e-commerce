import random
from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

# Simulated cart data
cart = []

# List of random items to choose from
items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 599.99},
    {"id": 3, "name": "Headphones", "price": 149.99},
    {"id": 4, "name": "Smart Watch", "price": 199.99},
    {"id": 5, "name": "Camera", "price": 499.99},
    {"id": 6, "name": "Keyboard", "price": 89.99},
    {"id": 7, "name": "Mouse", "price": 49.99},
    {"id": 8, "name": "Monitor", "price": 249.99},
    {"id": 9, "name": "Tablet", "price": 399.99},
    {"id": 10, "name": "Portable Charger", "price": 29.99}
]

@main.route('/')
def home():
    return jsonify({"message": "Welcome to the E-Commerce API"}), 200

@main.route('/cart', methods=['GET'])
def view_cart():
    if not cart:
        return jsonify({"message": "Your cart is empty"}), 200
    return jsonify({"message": "Items in your cart", "cart": cart}), 200

@main.route('/add-to-cart', methods=['GET'])
def add_to_cart():
    # Select a random item from the items list
    new_item = random.choice(items)
    cart.append(new_item)
    return jsonify({"message": f"Added {new_item['name']} to cart", "cart": cart}), 200

@main.route('/order', methods=['GET'])
def order():
    if not cart:
        return jsonify({"message": "Cart is empty"}), 200
    return jsonify({"message": "Order placed successfully", "order": cart}), 200

@main.route('/products', methods=['GET'])
def view_products():
    return jsonify({"products": items}), 200

@main.route('/clear-cart', methods=['GET'])
def clear_cart():
    cart.clear()
    return jsonify({"message": "Your cart has been cleared."}), 200
