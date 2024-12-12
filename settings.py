import mysql.connector
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Gourmet_db"
    )
    return conn


conn = connect_db()
cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE plats IF NOT EXISTS (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         custom BOOL,
#         name VARCHAR(50),
#         price INT
#     );
#             """)

cursor.execute("""
    CREATE TABLE plats_ingredients (
        plat_id INT,
        ingredient_id INT,
        PRIMARY KEY (plat_id, ingredient_id),
        FOREIGN KEY (plat_id) REFERENCES plats(id) ON DELETE CASCADE,
        FOREIGN KEY (ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
    );
                           """)

# cursor.execute("""
# CREATE TABLE commandes (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     client_name INT,
#     status BOOL,
#     total FLOAT,
# );
#           """)

# cursor.execute("""
# CREATE TABLE plats_commandes (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     plat_id INT,
#     commandes_id INT,
#     quantity INT,
#     FOREIGN KEY (plat_id) REFERENCES plats(id) ON DELETE CASCADE,
#     FOREIGN KEY (commandes_id) REFERENCES ingredients(id) ON DELETE CASCADE
# );
#                                         """)