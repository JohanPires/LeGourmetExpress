from settings import connect_db

conn = connect_db()
cursor = conn.cursor()

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


class Product:
       
    def add_product(name, custom, price):
        cursor.execute("""
            INSERT INTO products (name, custom, price) 
            VALUES (%s, %s, %s)
            """, (name, custom, price))
        conn.commit()

    def get_products():
        cursor.execute('SELECT * FROM products')
        resultats = cursor.fetchall()
        for product in resultats:
            if(product[1] == 0):
                print(product)

    def get_one_product(name):
        cursor.execute('SELECT * FROM products WHERE name = %s and custom = 0', (name,))
        resultats = cursor.fetchall()
        for product in resultats:
            print(product)

    def custom_product(name, custom, price):
        cursor.execute("""
            INSERT INTO products (name, custom, price) 
            VALUES (%s, %s, %s)
            """, (name, custom, price))
        conn.commit()

    def get_product_with_ingredients(name):
        cursor.execute("""
            SELECT p.id, p.name, p.custom, p.price, i.name AS ingredient_name
            FROM products p
            LEFT JOIN product_ingredients pi ON p.id = pi.products_id
            LEFT JOIN ingredients i ON pi.ingredients_id = i.id
            WHERE p.name = %s
        """, (name,))
        resultats = cursor.fetchall()
        for product in resultats:
            print(product)

    
    
