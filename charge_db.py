from settings import connect_db

conn = connect_db()
cursor = conn.cursor()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Coca-Cola", 2.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Nestea", 2.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Fanta", 2.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Kebab", 6.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Frites", 2.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Sauce algérienne", 0.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Sauce blanche", 0.00))
conn.commit()

cursor.execute("INSERT INTO products (custom, name, price) VALUES (%s, %s, %s)", (False, "Sauce samouraï", 0.00))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Portion de frites", 400))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Tomate", 400))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Salade", 600))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Oignon", 600))
conn.commit()

cursor.execute("INSERT INTO ingredients (name, stock) VALUES (%s, %s)", ("Pain à kebab", 600))
conn.commit()