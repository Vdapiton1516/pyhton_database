# JOINing data from multiple tables
import sqlite3

# sqlite3 database connection
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cur = conn.cursor()

# Create Table
cur.execute("""CREATE TABLE orders (make TEXT, model TEXT, order_date DATE) """)

order = [
    ('Ford', 'Ford_01', '2019-01-01'),
    ('Ford', 'Ford_01', '2019-01-02'),
    ('Ford', 'Ford_01', '2019-01-03'),
    ('Ford', 'Ford_02', '2019-02-01'),
    ('Ford', 'Ford_02', '2019-02-02'),
    ('Ford', 'Ford_02', '2019-02-03'),
    ('Ford', 'Ford_03', '2019-02-01'),
    ('Ford', 'Ford_03', '2019-02-02'),
    ('Ford', 'Ford_03', '2019-02-03'),
    ('Honda', 'Honda_01', '2019-01-01'),
    ('Honda', 'Honda_01', '2019-01-02'),
    ('Honda', 'Honda_01', '2019-01-03'),
    ('Honda', 'Honda_02', '2019-02-01'),
    ('Honda', 'Honda_02', '2019-02-02'),
    ('Honda', 'Honda_02', '2019-02-03')
    ]

cur.executemany("INSERT INTO orders VALUES(?, ?, ?)", order)

cur.execute("SELECT * FROM orders")

rows = cur.fetchall()
for r in rows:
    print("Make: " + r[0])
    print("Model: " + str(r[1]))
    print("Order Date: " + r[2])
    print("")


# commit the changes

conn.commit()
# close the database connection
conn.close()