import sqlite3


def create_database():

    connection = sqlite3.connect(":memory:")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        INSERT INTO products (product_id, product_name, price, quantity)
        VALUES (1, 'Sauce Labs Backpack', 29.99, 1)
    """)

    connection.commit()

    return connection


def get_product(connection, product_name):

    cursor = connection.cursor()

    cursor.execute("""
        SELECT product_name, price, quantity
        FROM products
        WHERE product_name = ?
    """, (product_name,))

    return cursor.fetchone()