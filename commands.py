from settings import connect_db

conn = connect_db()
cursor = conn.cursor()


def menu_command(cursor, conn):
    print("1. Create a command")
    print("2. Update a command")
    print("4. Show all commands")
    print("5. Show a command")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        #     create_command(cursor, conn)
        # elif choice == "2":
        #     update_command(cursor, conn)
        # elif choice == "4":
        #     show_all_commands(cursor, conn)
        # elif choice == "5":
        #     show_command(cursor, conn)
        # elif choice == "6":
        exit()
    else:
        print("Invalid choice")
        menu_command(cursor, conn)


def commands(cursor, conn):
    pass
