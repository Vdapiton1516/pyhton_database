# JOINing data from multiple tables
import sqlite3

# sqlite3 database connection
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cur = conn.cursor()

# SQL JOINS
 # retrieve data
cur.execute("""SELECT inventory.make, inventory.model,
            inventory.quantity, orders.order_date FROM inventory INNER JOIN orders
            ON inventory.model = orders.model""")

rows = cur.fetchall()

for r in rows:
    print(r[0], r[1])
    print(r[2])
    print(r[3])
    print()


# commit the changes


conn.commit()
# close the database connection
conn.close()