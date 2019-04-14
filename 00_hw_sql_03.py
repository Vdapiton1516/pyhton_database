# UPDATE and DELETE statements
import sqlite3
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
# update data
    c.execute("UPDATE inventory SET quantity = 100 WHERE make='Honda'")

c.execute("SELECT * FROM inventory")
rows = c.fetchall()
for r in rows:
    print(r[0], r[1], r[2])

# commit the changes
    c.commit()

# close the database connection
    c.close()    