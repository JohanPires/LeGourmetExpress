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
