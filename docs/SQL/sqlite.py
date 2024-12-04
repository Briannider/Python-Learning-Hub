"""
This script creates a SQLite database and a table named 'stock' to manage video game inventory.

The 'stock' table stores video game info: id, name, price, quantity, category and platforms.
"""

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
con = sqlite3.connect("database.db")

# Create a cursor object to interact with the database
cur = con.cursor()

# Execute a SQL command to create the 'stock' table if it doesn't already exist
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each video game
        name TEXT NOT NULL,                    -- Name of the video game
        price INTEGER,                         -- Price of the video game
        quantity INTEGER,                      -- Quantity in stock
        category TEXT,                         -- Category of the video game
        platforms TEXT                         -- Platforms on which the video game is available
    )
    """
)
# Commit the changes to the database
con.commit()

# Check if the database connection is working by executing a simple query
try:
    cur.execute("SELECT 1")
    print("Database is working")
except sqlite3.Error as e:
    print(f"Database error: {e}")

# Insert data into the 'stock' table
# The ? placeholder is used to avoid SQL injection attacks
# cur.execute(
#     """
#     INSERT INTO stock (name, price, quantity, category, platforms) VALUES
#         (?, ?, ?, ?, ?)
# """,
#     (
#         "Dark Souls 3 ",  # Name
#         100,  # Price
#         20,  # Quantity
#         "Action-adventure",  # Category
#         "PC",  # Platforms
#     ),
# )

# Commit the changes to the database
con.commit()

# Fetch all rows from the 'stock' table
res = cur.execute("SELECT * FROM stock")

# Fetch the first row
res.fetchone()

# Iterate over each row in the table
for row in res:
    print(row)


con.close()
