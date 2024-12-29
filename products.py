from settings import connect_db
from ingredients import Ingredient

conn = connect_db()
cursor = conn.cursor()


class Product:
       

    def get_products():
        cursor.execute('SELECT * FROM products')
        resultats = cursor.fetchall()
        for product in resultats:
            if(product[1] == 0):
                print(f'{product[0]}: {product[2]}')
  
    def get_one_product(name):
        cursor.execute('SELECT * FROM products WHERE name = %s', (name,))
        resultats = cursor.fetchall()
        for product in resultats:
            print(product)

    def create_custom_product():
        name = str(input("Quel sera le nom de ce produit personnalisé? "))
        price = float(input("Quel sera le prix de ce produit personnalisé? "))
        cursor.execute("""
            INSERT INTO products (name, custom, price) 
            VALUES (%s, 1, %s)
            """, (name, price))
        conn.commit()
        product_id = cursor.lastrowid
        while True:
            add_ingredient = int(input("Tapez 1 pour ajouter un ingrédient au produit personnalisé, tapez 0 si le produit est déjà complet. "))
            if add_ingredient == 1:
                Product.add_ingredient_to_product(product_id)
            elif add_ingredient == 0:
                print(f"Le produit personnalisé {name} est complet.\n")
                return product_id
            else:
                print("Entrée invalide. Veuillez taper 1 pour ajouter un ingrédient ou 0 pour terminer.")
    
    def add_ingredient_to_product(product_id):
        Ingredient.get_ingredients()
        ingredient_id = int(input("\nTapez le numéro d'ingrédient que vous souhaitez ajouter au produit personnalisé. "))
        cursor.execute("""
            INSERT INTO product_ingredients (product_id, ingredient_id) 
            VALUES (%s, %s)
            """, (product_id, ingredient_id))
        conn.commit()
        print(f"\nIngrédient {ingredient_id} ajouté au produit {product_id}.")

    def get_product_with_ingredients(id):
        cursor.execute("""
            SELECT 
                p.id, 
                p.name, 
                p.custom, 
                p.price, 
                GROUP_CONCAT(i.name SEPARATOR ', ') AS ingredients
            FROM products p
            LEFT JOIN product_ingredients pi ON p.id = pi.product_id
            LEFT JOIN ingredients i ON pi.ingredient_id = i.id
            WHERE p.id = %s
            GROUP BY p.id, p.name, p.custom, p.price
            """, (id,))
        resultats = cursor.fetchall()
        print(f'Le produit {resultats[0][1]} est constitué de :') 
        array = resultats[0][4].split(', ')
        
        for ingredient in array : 
            print(ingredient)