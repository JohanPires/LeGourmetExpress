from settings import connect_db

conn = connect_db()
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        stock INT
    );
            """)

class Ingredient:
    
    def get_ingredient():
        cursor.execute('SELECT * FROM ingredients')
        resultats = cursor.fetchall()
        for book in resultats:
            print(book)



