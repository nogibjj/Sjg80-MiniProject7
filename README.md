# Sjg80-MiniProject7
Package a Python Script into a Command-Line Tool 

```markdown
# My Command-Line Tool

My Command-Line Tool is a Python script that allows you to manage a SQLite database of users from the command line. It provides functionality for creating a database, adding users, and performing various database operations.

## Installation

To use My Command-Line Tool, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/my-command-line-tool.git
   cd my-command-line-tool
   ```

2. Install the tool:
   ```bash
   pip install .
   ```

## Usage

My Command-Line Tool is simple to use. Here are the basic commands:

- To create a database:
   ```bash
   my_tool create_db database.db
   ```

- To add a user to the database:
   ```bash
   my_tool add_user database.db --username JohnDoe --email john@example.com
   ```

- To perform various database operations:
   ```bash
   my_tool operate database.db --operation some_operation
   ```

## Options
- `create_db`: Create a new database file.
- `add_user`: Add a new user to the database.
- `operate`: Perform various database operations.
