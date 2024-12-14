from ingredients import Ingredient
from products import Product
from commands import menu_command


def menu_cuisiner():
    while True:
        print("\n--- Menu Cuisinier---")
        print("1. Accéder aux commandes")
        # print("2. Lire les commandes")
        # print("3. Mettre à jour une commande")
        # print("4. Créer un produit")
        # print("5. Lire les produits")
        # print("6. Lire les ingrédients")
        print("7. Quitter")

        choix = input("Choisissez une option : ")
        if choix == "1":


    # afficher les commandes en status waiting
    choice_command = input("Choisissez le numéro de la commande à traiter : ")
    # afficher la commande sélectionner via l'id entrer par le cuisiner
    Product.get_product_with_ingredients(name)
    update_status = input(
        "Indique à tous que tu cuisines ces plats avec le statut 'cooking' : ")
    # update le status de la commande
    # récupérer la liste des ingrédients présents dans get_product_with_ingredient
    # boucle pour la MAJ du stock des ingredients
    Ingredient.update_ingredients(id)