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
        print("3. Voir toutes les commandes prêtes et les délivrer au client")
        print("4. Accéder aux détails des produits")
        print("5. Consulter les ingrédients et les stocks")
        print("6. Quitter\n")

        choice = input("Choisissez une option : ")

        if choice == "1":
            print("Création d'une commande\n")
            client = input("Nom du client ? ")
            
            command_id = Command.save(client, "waiting", 0)
            
            print(f"La commande a bien été créée.\n")
            
            while True:
                Product.get_classic_products()
                product_id = int(input('\nEntrez un numéro de produit commandé par le client ou entrez 0 si le client veut commander un produit personnalisé: '))
                if product_id == 0:
                    product_id = Product.create_product(1)
                quantity = int(input("\nChoisissez la quantité de ce produit commandée par le client: "))
                Command.add_product_to_command(int(command_id), int(product_id), int(quantity))               
                add_product = input("\nVoulez-vous ajouter un produit à la commande? Oui ou non? ")
                if (add_product == "non"):
                    Command.calculate_total_price(command_id)
                    return False
              
        elif choice == "2":
            Command.get_commands()
        
        elif choice == "3":
            Command.get_ready_commands()
            command_id = input("Choisissez le numéro de commande que vous souhaitez délivrer au client : ")
            Command.update_command_status(command_id, "collected")
            print("\n")
            print("---------FACTURE---------")
            Command.get_one_command_with_products(command_id)

        elif choice == "4":
            Product.get_all_products()
            product_id = input("Choisissez le numéro du produit que vous souhaitez consulter : ")
            Product.get_product_with_ingredients(product_id)
        
        elif choice == "5":
            Ingredient.get_ingredients()
            
        elif choice == "6":
            print("Retour au menu principal...")
            break

        else:
            print("Option invalide. Veuillez réessayer.")


