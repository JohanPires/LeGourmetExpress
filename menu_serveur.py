from products import Product
from commands import Command
from ingredients import Ingredient
from settings import connect_db
conn = connect_db()
cursor = conn.cursor() 



def menu_serveur(): 
    while True:
        print("\n--- Menu Serveur ---")
        print("1. Créer une commande")
        print("2. Lire les commandes")
        # print("3. Mettre à jour une commande")
        # print("4. Créer un produit")
        print("5. Lire les produits")
        print("6. Consulter les ingrédients et les stocks")
        print("7. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            print("Création d'une commande")
            print("\n")
            client = input("Nom du client ? ")
            
            Command.save(client, "waiting", 0)
            
            print(f"La commande a bien été créée.")

            cursor.execute("SELECT id FROM commands ORDER BY id DESC LIMIT 1")
            command_id = int(cursor.fetchone()[0])
            
            while True:
                Product.get_products()
                product_id = int(input('Entrer un numéro de produit commandé par le client : '))
                quantity = int(input("Choisissez une quantité : "))
                Command.add_product_to_command(int(command_id), int(product_id), int(quantity))               
                add_product = input("Voulez-vous ajouter un produit? Oui ou non?")
                if (add_product == "non"):
                    Command.calculate_total_price(command_id)
                    return False
              
      
        elif choice == "2":
            Command.get_commands()

        elif choice == "5":
            Product.get_products()
            product_id = input("Choisissez le numéro du produit que vous souhaitez consulter : ")
            Product.get_product_with_ingredients(product_id)
        
        elif choice == "6":
            Ingredient.get_ingredients()
            
        elif choice == "7":
            print("Retour au menu principal...")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


