from settings import connect_db

conn = connect_db()
cursor = conn.cursor()


class Ingredient:
    def get_ingredients():
        cursor.execute('SELECT * FROM ingredients')
        resultats = cursor.fetchall()
        for ingredient in resultats:
            print(f"{ingredient[1]}, stock actuel: {ingredient[2]}")

    def update_stock_ingredient(ingredient_id, new_stock):
        cursor.execute(
            "UPDATE ingredients SET stock = %s WHERE id = %s", (new_stock, ingredient_id))
        conn.commit()
        print("Le stock a bien été mis à jour.")


