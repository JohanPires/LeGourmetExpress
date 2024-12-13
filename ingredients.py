from settings import connect_db

conn = connect_db()
cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS ingredients (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(50),
#         stock INT
#     );
#             """)


class Ingredient:
    # def init():

    # def add_product():
    #     cursor.execute("""
    #         INSERT INTO products (name, custom, price)
    #         VALUES (%s, %s, %s)
    #         """, ('coca', False, 20))
    #     conn.commit()

    def get_ingredient():
        cursor.execute('SELECT * FROM ingredients')
        resultats = cursor.fetchall()
        for book in resultats:
            print(book)

    def update_ingredients(id):
        cursor.execute("SELECT stock FROM ingredients WHERE id = %s", (id))
        result = cursor.fetchall()
        new_count = result - 1
        cursor.execute(
            "UPDATE ingredients SET stock = %s WHERE name = %s", (new_count, id))
        conn.commit()

    get_ingredient()
    update_ingredients()
