#  This file will be only executed one time and creates the tables and relationships 
import sqlite3
# from datetime import datetime
from config import DATABASE_NAME
from app.data.initial_data import get_prices_table


def create_tables(cursor):
     
     cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                         id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL
                         );
                    """)

     cursor.execute("""CREATE TABLE IF NOT EXISTS brands (
                         id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL
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
                         curr VARCHAR(3),
                         FOREIGN KEY (brand_id) REFERENCES brands(id),
                         FOREIGN KEY (product_id) REFERENCES products(id)
                         );
                    """)

def insert_initial_data(cursor):
     cursor.execute("INSERT INTO products VALUES (35455, 'product1')")
     cursor.execute("INSERT INTO brands VALUES (1, 'STORE_x')")
     cursor.executemany("INSERT INTO prices VALUES (?,?,?,?,?,?,?,?)", get_prices_table())
     
# this function take the data and creates the database with that data
def create_database():
     # Connection to the database
     conn = sqlite3.connect(DATABASE_NAME)
     # cursor for db creation
     cursor = conn.cursor()
     # create tables
     create_tables(cursor)
     # Insert values into database
     insert_initial_data(cursor)

     print("Database created successfully")

     conn.commit()
     conn.close()
     
     
     
if __name__ == "__main__":
     create_database()