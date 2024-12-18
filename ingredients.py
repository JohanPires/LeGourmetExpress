from settings import connect_db

conn = connect_db()
cursor = conn.cursor()


class Ingredient:
    def get_ingredients():
        cursor.execute('SELECT * FROM ingredients')
        resultats = cursor.fetchall()
        for ingredient in resultats:
            print(f"{ingredient[1]}, stock actuel: {ingredient[2]}")

    def decrement_stock_ingredient(id):
        cursor.execute("SELECT stock FROM ingredients WHERE id = %s", (id))
        actual_stock = cursor.fetchall()
        new_stock = actual_stock - 1
        cursor.execute(
            "UPDATE ingredients SET stock = %s WHERE id = %s", (new_stock, id))
        conn.commit()


