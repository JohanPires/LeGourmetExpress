from settings import connect_db

conn = connect_db()
cursor = conn.cursor()


class Ingredient:
    def get_ingredients():
        cursor.execute('SELECT * FROM ingredients')
        resultats = cursor.fetchall()
        for ingredient in resultats:
            print(ingredient)

    def update_ingredients(id):
        cursor.execute("SELECT stock FROM ingredients WHERE id = %s", (id))
        result = cursor.fetchall()
        new_count = result - 1
        cursor.execute(
            "UPDATE ingredients SET stock = %s WHERE id = %s", (new_count, id))
        conn.commit()

    get_ingredients()
    update_ingredients()
