from settings import connect_db

conn = connect_db()
cursor = conn.cursor()


cursor.execute(""" 
    CREATE TABLE ingredients IF NOT EXISTS(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
               quantity INT
               )
            """)
conn.commit()

# ------------ Classe ---------------#


class ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
