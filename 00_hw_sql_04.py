# UPDATE and DELETE statements
import sqlite3
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

# Output sql
c.execute("SELECT * FROM inventory WHERE make ='Ford'")
rows = c.fetchall()

 # output headers
print('Make Model Qty')
print('--------------')

for r in rows:
    print(r[0], r[1], r[2])


# close the database connection
    c.close()    