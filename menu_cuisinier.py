from ingredients import Ingredient
from products import Product
from commands import Command
from settings import connect_db
conn = connect_db()
cursor = conn.cursor() 


def menu_cuisinier():
    while True:
        print("\n--- Menu Cuisinier---")
        print("1. Accéder à toutes les commandes")
        print("2. Lire le détail d'une commande en cours")
        print("3. Mettre à jour une commande")
        print("4. Créer un produit")
        print("5. Lire les produits")
        print("6. Consulter/modifier les stocks d'ingrédients")
        print("7. Rapport journalier des ventes")
        print("8. Quitter")

        choice = input("Choisissez une option : ")
        if choice == "1":
            Command.get_commands()

        elif choice == "2":
            Command.get_waiting_commands()
            command_id = input("Choisissez le numéro de commande que vous souhaitez consulter : ")
            Command.get_one_command_with_products(command_id)

        elif choice == "3":
            Command.get_commands()
            command_id = input("Choisissez le numéro de commande que vous souhaitez modifier : ")
            ready = input("Cette commande est-elle prête? Oui ou non? ")
            if ready == "oui":
                Command.update_command_status(command_id, "ready")
                print(f"La commande n°{command_id} a bien été mise à jour.")

        elif choice == "4":
            print("Cette fonctionnalité n'a pas encore été implémentée.")

        elif choice == "5":
            Product.get_products()
            product_id = input("Choisissez le numéro du produit que vous souhaitez consulter : ")
            Product.get_product_with_ingredients(product_id)

        elif choice == "6":
            Ingredient.get_ingredients()
            update = input("Souhaitez-vous mettre à jour le stock d'un ingrédient? Oui ou non? ")
            if update == "oui":
                ingredient_id = input("Choisissez le numéro de l'ingrédient que vous souhaitez mettre à jour : ")
                new_stock = input("Quelle est le nouveau stock ? ")
                Ingredient.update_stock_ingredient(ingredient_id, new_stock)

        elif choice == "7":
            Command.daily_sales_report()

        elif choice == "8":
            print("Retour au menu principal...")
            break

        else:
            print("Option invalide. Veuillez réessayer.")