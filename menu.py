from menu_serveur import menu_serveur
from menu_cuisinier import menu_cuisinier


def principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Serveur")
        print("2. Cuisinier")
        print("3. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            menu_serveur()
        elif choix == "2":
            menu_cuisinier() 
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    principal()
