from settings import connect_db

conn = connect_db()
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        stock INT
    );
            """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        custom BOOLEAN,
        name VARCHAR(50),
        price DOUBLE
    );
            """)


cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_ingredients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        products_id INT,
        ingredients_id INT,
        FOREIGN KEY (products_id) REFERENCES products(id) ON DELETE CASCADE,
        FOREIGN KEY (ingredients_id) REFERENCES ingredients(id) ON DELETE CASCADE
    );
            """)

cursor.execute("""
            CREATE TABLE commands (
                id INT AUTO_INCREMENT PRIMARY KEY,
                client_name VARCHAR(50),
                status VARCHAR(20),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_price DOUBLE
            );
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS command_products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            command_id INT,
            product_id INT,
            quantity INT
        );
""")


cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Coca-Cola", 2.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Nestea", 2.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Fanta", 2.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Kebab", 6.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Frites", 2.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Sauce algérienne", 0.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Sauce blanche", 0.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Sauce samouraï", 0.00))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Portion de frites", 400))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Tomate", 400))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Salade", 600))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Oignon", 600))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Pain à kebab", 600))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Coca-Cola", 600))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Viande", 600))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Fanta", 600))
# conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Sauce algérienne", 600))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Sauce blanche", 600))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Sauce samouraÏ", 600))
conn.commit()


# Coca-Cola

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (1, 6))
conn.commit()


# Kebab

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (4, 2))
conn.commit()

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (4, 3))
conn.commit()

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (4, 4))
conn.commit()

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (4, 5))
conn.commit()

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (4, 7))
conn.commit()


# Fanta

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (3, 8))
conn.commit()

# Nestea

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (2, 6))
conn.commit()

# Frites

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (5, 1))
conn.commit()

# Sauce samouraï

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (8, 11))
conn.commit()

# Sauce blanche

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (7, 10))
conn.commit()

# Sauce algérienne

cursor.execute("INSERT INTO product_ingredients (products_id, ingredients_id) VALUES (%s, %s)", (6, 9))
conn.commit()