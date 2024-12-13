from ingredients import Ingredient
from products import Product
from commands import menu_command


def menu_cuisiner():
    # afficher les commandes en status waiting
    choice_command = input("Choisissez le numéro de la commande à traiter : ")
    # afficher la commande sélectionner via l'id entrer par le cuisiner
    Product.get_one_product(argument)
    update_status = input(
        "Indique à tous que tu cuisines ces plats avec le statut 'cooking' : ")
    # update le status de la commande
