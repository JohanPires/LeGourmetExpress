from settings import connect_db

conn = connect_db()
cursor = conn.cursor()


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
                print(f'{product[0]}: {product[2]}')
  
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

    def get_product_with_ingredients(id):
        cursor.execute("""
            SELECT 
                p.id, 
                p.name, 
                p.custom, 
                p.price, 
                GROUP_CONCAT(i.name SEPARATOR ', ') AS ingredients
            FROM products p
            LEFT JOIN product_ingredients pi ON p.id = pi.products_id
            LEFT JOIN ingredients i ON pi.ingredients_id = i.id
            WHERE p.id = %s
            GROUP BY p.id, p.name, p.custom, p.price
            """, (id,))
        resultats = cursor.fetchall()
        print(f'Le produit {resultats[0][1]} est constitué de :') 
        array = resultats[0][4].split(', ')
        
        for ingredient in array : 
            print(ingredient)
        # custom = input("Valider la commande ou modifier un ingédients (Oui ou nom d'un ingrédients)")
        # if(custom == 'oui'):
    
        

    
    
