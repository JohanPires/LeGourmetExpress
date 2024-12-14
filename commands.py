from settings import connect_db
from products import Product

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
        print(result[0]) 

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
            print(command)

    def get_one_command_with_products(id):
        cursor.execute("""
            SELECT c.id, c.client_name, c.status, c.created_at, c.total_price, p.name, cp.quantity
            FROM commands c
            LEFT JOIN command_products cp ON c.id = cp.command_id
            LEFT JOIN products p ON cp.product_id = p.id
            WHERE c.id = %s
            """, (id,))
        resultats = cursor.fetchall()
        for command in resultats:
            print(command)

   
def command_nav():
    while True:
        print("1. Create command")
        print("2. Show all commands")
        print("3. Show one command with products")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            input_client_name = input("Enter client name: ")
            input_status = Status.select_status()
            input_created_at = input("Enter created at: ")
            input_total_price = input("Enter total price: ")
            command = Command(input_client_name, input_status, input_created_at, input_total_price)
            command.save()

        elif choice == "2":
            Command.get_commands()
        elif choice == "3":
            id = input("Enter command id: ")
            Command.get_one_command_with_products(id)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

# command_nav()
