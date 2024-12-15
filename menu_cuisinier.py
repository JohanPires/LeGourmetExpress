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
        # print("3. Mettre à jour une commande")
        # print("4. Créer un produit")
        print("5. Lire les produits")
        print("6. Lire les ingrédients")
        print("7. Quitter")

        choix = input("Choisissez une option : ")
        if choix == "1":
            Command.get_commands()
        elif choix == "2":
            Command.get_waiting_commands()
            command_id = input("Choisissez le numéro de commande que vous souhaitez consulter : ")
            Command.get_one_command_with_products(command_id)
        elif choix == "5":
            Product.get_products()
            product_id = input("Choisissez le numéro du produit que vous souhaitez consulter : ")
            Product.get_product_with_ingredients(product_id)
    # update_status = input(
        # "Indique à tous que tu cuisines ces plats avec le statut 'cooking' : ")
    # update le status de la commande
    # récupérer la liste des ingrédients présents dans get_product_with_ingredient
    # boucle pour la MAJ du stock des ingredients
    # Ingredient.update_ingredients(id)
        elif choix == "6":
            Ingredient.get_ingredients()
        elif choix == "7":
            print("Retour au menu principal...")
            break
        else:
            print("Option invalide. Veuillez réessayer.")