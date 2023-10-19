import sqlite3
import click

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

# Function to create the 'users' table if it doesn't exist
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
    except sqlite3.Error as e:
        print(e)

# Function to insert a new user into the database
def insert_user(conn, username, email):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
                        (username, email))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

  def main(database_file):
    connection = create_connection(database_file)
    if connection:
        create_table(connection)
        # Create a new user
        insert_user(connection, "JohnDoe", "john@example.com")
        # Read a user
        user = get_user_by_username(connection, "JohnDoe")
        if user:
            print("User found:", user)
        # Update user email
        update_user_email(connection, "JohnDoe", "new_email@example.com")
        # Read the updated user
        updated_user = get_user_by_username(connection, "JohnDoe")
        if updated_user:
            print("Updated user:", updated_user)
        # Delete the user
        delete_user(connection, "JohnDoe")
        # user with shortest email
        insert_user(connection, "Apple", "a@example.com")
        insert_user(connection, "Banana", "Banana@example.com")
        insert_user(connection, "Orange", "ora@example.com")
        person = select_person_with_shortest_email(connection)
        if person:
            print("Person with the shortest email:")
            print("User ID:", person[0])
            print("Username:", person[1])
            print("Email:", person[2])
        else:
            print("No users in the database.")
        # select all users
        users = select_all_users(connection)
        for user in users:
            print("User ID:", user[0])
            print("Username:", user[1])
            print("Email:", user[2])

        connection.close()


if __name__ == "__main__":
    main()
