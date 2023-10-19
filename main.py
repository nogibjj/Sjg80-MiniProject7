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
        if user:
            print("User found:", user)
  
        connection.close()

if __name__ == "__main__":
    main()
