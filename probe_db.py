import sqlite3


conn = sqlite3.connect('webstore.db')

c = conn.cursor()

# c.execute("SELECT * FROM prices")

    
c.execute("""
          SELECT prices.product_id, products.name
          FROM prices
          JOIN products ON prices.product_id = products.id;
          """)

result = c.fetchall()

for row in result:
    print(row)
    
conn.commit()

conn.close()