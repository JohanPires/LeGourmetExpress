from commands import commands as cmd
from settings import connect_db

conn = connect_db()
cursor = conn.cursor()

def main(cursor, conn):
    cmd(cursor, conn)

main(cursor, conn)