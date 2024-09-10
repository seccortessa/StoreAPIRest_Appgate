#  This file will be only executed one time and creates the tables an relationships 
import sqlite3
from datetime import datetime

prices_table = [
                    (1, datetime(2020, 6, 14), datetime(2020, 12, 31, 23, 59, 59), 1, 35455, 0, 32.5, 'USD'),
                    (1, datetime(2020, 6, 14), datetime(2020, 6, 14, 18, 30, 00), 2, 35455, 1, 25.45, 'USD'),
                    (1, datetime(2020, 6, 14), datetime(2020, 6, 15, 11, 00, 00), 3, 35455, 1, 30.5, 'USD'),
                    (1, datetime(2020, 6, 14), datetime(2020, 12, 31, 23, 59, 59), 4, 35455, 1, 38.95, 'USD')
                ]

# Connection to the database
conn = sqlite3.connect("webstore.db")

# cursor for db creation
cursor = conn.cursor()

# create tables
cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    NAME TEXT NOT NULL
                    );
               """)

cursor.execute("""CREATE TABLE IF NOT EXISTS brands (
                    id INTEGER PRIMARY KEY,
                    NAME TEXT NOT NULL
                    );
               """)

cursor.execute("""CREATE TABLE IF NOT EXISTS prices (
                    brand_id INTEGER,
                    start_date DATETIME,
                    end_date DATETIME,
                    price_list INTEGER,
                    product_id INTEGER,
                    priority INTEGER,
                    price DECIMAL,
                    curr VARCHAR(3)
                    );
               """)

# Insert values into database

cursor.execute("INSERT INTO products VALUES (35455, 'product1')")

cursor.execute("INSERT INTO brands VALUES (1, 'STORE_x')")

cursor.executemany("INSERT INTO prices VALUES (?,?,?,?,?,?,?,?)", prices_table)

print("Database created successfully")

conn.commit()
conn.close()