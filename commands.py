from settings import connect_db
from products import Product
import datetime

conn = connect_db()
cursor = conn.cursor()
class Status:
    WAITING = "waiting"
    COOKING = "cooking"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    UNKNOWN = "unknown"
    
    def select_status():
        print("1. Waiting")
        print("2. Cooking")
        print("3. Confirmed")
        print("4. Canceled")
        print("5. Unknown")
        choice = input("Enter status: ")
        if choice == "1":
            return Status.WAITING
        elif choice == "2":
            return Status.COOKING
        elif choice == "3":
            return Status.CONFIRMED
        elif choice == "4":
            return Status.CANCELED
        elif choice == "5":
            return Status.UNKNOWN
        else:
            return Status.UNKNOWN


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
