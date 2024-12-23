# E-Commerce Mock API

## Overview

This is a simple E-Commerce API built with Flask. The app allows users to interact with products, add items to their cart, place orders, and view available products. It is also Dockerized to ensure portability and easy deployment across different environments.

## Features

### Routes:

- `/`: A welcome message to greet users.
- `/cart`: View the current items in your shopping cart.
- `/add-to-cart`: Adds a random product to the shopping cart (GET request).
- `/order`: Place an order with the items currently in your cart.
- `/products`: View a list of available products.
- `/clear-cart`: Clear all items in the cart.

### Random Product List:

The app features a list of 10 randomly chosen products, such as:
- Laptop
- Smartphone
- Headphones
- Camera
- Smart Watch
- Tablet, etc.

### Cart System:

- Users can add products to their cart by visiting the `/add-to-cart` endpoint, which adds a random product.
- Users can view the cart to see the current items and their prices.
- The cart can be cleared with the `/clear-cart` route.
- Users can place an order by visiting `/order`, which displays the contents of the cart.

## Phases of Development

### Phase 1: API Development

In Phase 1, we developed the core functionality of the app:

- **API Routes**: Implemented basic routes for home, viewing the cart, adding to the cart, viewing products, placing an order, and clearing the cart.
- **Random Product List**: A list of 10 items was created, from which random items are selected when adding to the cart.
- **Cart Management**: Users can add random products to the cart, view the cart contents, and clear the cart.
- **Unit Tests**: Added basic tests to check the `/products`, `/add-to-cart`, and `/clear-cart` functionality.

#### Test Cases:
- `test_get_products(client)`: Verifies that the `/products` endpoint returns a list of products.
- `test_add_to_cart(client)`: Verifies that a random product is added to the cart.
- `test_clear_cart(client)`: Verifies that the cart is cleared when using the `/clear-cart` route.

### Phase 2: Dockerization

In Phase 2, we focused on Dockerizing the Flask application:

- **Dockerfile**: Created a Dockerfile to set up the environment and run the Flask app in a Docker container.
- **Docker Ignore**: Added a `.dockerignore` file to exclude unnecessary files from the Docker image.
- **Requirements File**: Added a `requirements.txt` file to list the dependencies needed for the app to run.
- **Build and Run**: 
  - Built the Docker image using `docker build -t ecommerce-mock .`.
  - Ran the app inside a Docker container using `docker run -p 5000:5000 ecommerce-mock`.

The app is now fully Dockerized, ensuring it can be run consistently across different environments.

### Phase 3: CI/CD Integration (In Progress)

In Phase 3, we are integrating GitHub Actions to automate the build and deployment of the Dockerized app. The goal is to create a continuous integration/continuous deployment (CI/CD) pipeline that automatically triggers on changes to the repository and updates the application with the latest code changes.

#### Steps:
1. **GitHub Actions Setup**: Created a GitHub Actions workflow to build and push the Docker image to a container registry upon pushing changes to the main branch.
2. **Automated Deployment**: 
   - The workflow will trigger the deployment of the app to the Kubernetes cluster using k3s.
   - The deployment leverages **Helm** or **kubectl** commands to update the app within the cluster.
3. **External Access via Load Balancer (Klipper)**:
   - For external access, the app is exposed using a **Klipper LoadBalancer** on k3s, which will allocate an external IP for the app.
   - The deployment will be accessible through the load balancer, ensuring it can be accessed externally.

Once the GitHub Actions pipeline is set up and tested, the app will be able to automatically deploy the latest version, making the entire process more efficient and automated.

---

## Running the App Locally

To run the app locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-directory>
