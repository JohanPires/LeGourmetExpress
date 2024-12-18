# 🍽️ Le Gourmet Express

Welcome to **Le Gourmet Express**, a product and ingredient management application for restaurants. This application allows you to efficiently manage products, ingredients, and orders.

## ✨ Features

- **Product Management**: Add, retrieve, and customize products.
- **Ingredient Management**: Retrieve and update ingredient stocks.
- **Order Management**: Create and manage customer orders.

## 🏗️ Project Structure

- `products.py`: Contains the `Product` class to manage products.
- `ingredients.py`: Contains the `Ingredient` class to manage ingredients.
- `commands.py`: Contains `Command` class manage orders.
- `charge_db.py`: Initializes the database by creating the necessary tables.

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/JohanPires/LeGourmetExpress
    cd LeGourmetExpress
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the database and connection in the `charge_db.py` file.

## 🚀 Usage

1. Initialize the database:
    ```bash
    python charge_db.py
    ```

2. Run the application:
    ```bash
    python menu.py
    ```

## 🤝 Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you wish to make.