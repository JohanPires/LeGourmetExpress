from settings import connect_db
from products import Product
from datetime import date

conn = connect_db()
cursor = conn.cursor()


class Command:
    def __init__(self, client_name, status, created_at, total_price):
        self.client_name = client_name
        self.status = status
        self.created_at = created_at
        self.total_price = total_price

    def add_product_to_command(command_id, product_id, quantity):
        cursor.execute("""
            INSERT INTO command_products (command_id, product_id, quantity)
            VALUES (%s, %s, %s)
            """, (command_id, product_id, quantity))
        conn.commit()

    def show_command_products_list(command_id):
        cursor.execute("""
            SELECT p.name, cp.quantity, p.price
            FROM command_products cp
            LEFT JOIN products p ON cp.product_id = p.id
            WHERE cp.command_id = %s
            """, (command_id,))
        resultats = cursor.fetchall()
        for product in resultats:
            print(product)

    def calculate_total_price(command_id):
        cursor.execute("""
            SELECT SUM(p.price * cp.quantity)
            FROM command_products cp
            LEFT JOIN products p ON cp.product_id = p.id
            WHERE cp.command_id = %s
            """, (command_id,))
        result = cursor.fetchone()
        price = result[0]
        print(f"Le total de la commande est de {price}€.") 
        cursor.execute("""
                       UPDATE commands 
                       SET total_price = %s 
                       WHERE id = %s""", 
                       (price, command_id))
        conn.commit()

    def save(client_name, status, total_price):
        cursor.execute("""
            INSERT INTO commands (client_name, status, total_price)
            VALUES (%s, %s, %s)
            """, (client_name, status, total_price))
        conn.commit()

    def get_commands():
        cursor.execute('SELECT * FROM commands')
        resultats = cursor.fetchall()
        for command in resultats:
            print(f"Commande n°{command[0]} pour {command[1]} passée à {command[3].strftime("%d/%m/%Y %H:%M")}. Statut {command[2]}.")

    def get_waiting_commands():
        cursor.execute('SELECT * FROM commands WHERE status LIKE "waiting"')
        resultats = cursor.fetchall()
        for command in resultats:
            print(f"Commande n°{command[0]} pour {command[1]} passée à {command[3].strftime("%d/%m/%Y %H:%M")}. Statut {command[2]}.")

    def get_one_command_with_products(id):
        cursor.execute("""
            SELECT c.client_name, c.status, c.created_at, c.total_price, p.name, cp.quantity
            FROM commands c
            LEFT JOIN command_products cp ON c.id = cp.command_id
            LEFT JOIN products p ON cp.product_id = p.id
            WHERE c.id = %s
            """, (id,))
        
        command_details = cursor.fetchall()
    
        if not command_details:
            print("Commande non trouvée.")
            return
        
        print(command_details)
        print(f"Commande de {command_details[0][0]} passée à {command_details[0][2].strftime("%d/%m/%Y %H:%M")}")
        print(f"Statut : {command_details[0][1]}")
        print(f"Prix total : {command_details[0][3]}")
        print("Produits :")

        for detail in command_details:
            product_name = detail[4]
            quantity = detail[5]
            print(f" - {quantity} {product_name}")

    def update_command_status(command_id, status):
        cursor.execute("""
                       UPDATE commands 
                       SET status = %s 
                       WHERE id = %s""", 
                       (status, command_id))
        conn.commit()
        # Si le statut est "ready", decrémenter les stocks de chaque ingrédient lié à la commande
        if status == "ready":
            Command.decrement_stocks(command_id)
        

    def decrement_stocks(command_id):
        cursor.execute("""
            UPDATE ingredients i
            JOIN (
                SELECT pi.ingredients_id,
                    SUM(cp.quantity) AS qty_to_decrement
                FROM command_products cp
                JOIN product_ingredients pi ON cp.product_id = pi.products_id
                WHERE cp.command_id = %s
                GROUP BY pi.ingredients_id
            ) AS subquery ON i.id = subquery.ingredients_id
            SET i.stock = i.stock - subquery.qty_to_decrement;
            """, 
            (command_id,)
        )
        conn.commit()
    
    def daily_sales_report():
        current_day = date.today()
        print(f"\n--- Rapport journalier du {current_day} --- \n")
        cursor.execute("""
            SELECT id, total_price, DATE_FORMAT(created_at, "%H:%i")
            FROM commands
            WHERE DATE(created_at) = %s
            ORDER BY id
        """,
        (current_day,))
        commands = cursor.fetchall()

        total_sales = 0

        for command in commands:
            command_id, total_price, created_at = command
            total_sales += total_price
            print(f"Commande passée à {created_at} pour un total de {total_price}€ contenant :")
            cursor.execute("""
                SELECT p.name, cp.quantity
                FROM command_products cp
                JOIN products p ON cp.product_id = p.id
                WHERE cp.command_id = %s
            """, (command_id,))
            
            products = cursor.fetchall()

            for product in products:
                product_name, quantity = product
                print(f"   - Produit: {product_name}, Quantité: {quantity}")
            print("\n")

        print(f"Total des ventes pour le {current_day} : {total_sales}€")