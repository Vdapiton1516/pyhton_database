# Create a table and populate it with data
import sqlite3

# sqlite3 database connection
conn = sqlite3.connect("new.db")
# get a cursor object used to execute SQL commands
cur = conn.cursor()

   # c.execute("""CREATE TABLE regions (city TEXT, region TEXT) """)
# (again, copy and paste the values if you'd like)
cities = [
    ('New York City', 'Northeast'),
    ('San Francisco', 'West'),
    ('Chicago', 'Midwest'),
    ('Houston', 'South'),
    ('Phoenix', 'West'),
    ('Boston', 'Northeast'),
    ('Los Angeles', 'West'),
    ('Houston', 'South'),
    ('Philadelphia', 'Northeast'),
    ('San Antonio', 'South'),
    ('San Diego', 'West'),
    ('Dallas', 'South'),
    ('San Jose', 'West'),
    ('Jacksonville', 'South'),
    ('Indianapolis', 'Midwest'),
    ('Austin', 'South'),
    ('Detroit', 'Midwest')
    ]


cur.executemany("INSERT INTO regions(city, region) values (?, ?)", cities)
cur.execute("SELECT * FROM regions ORDER BY region ASC")
rows = cur.fetchall()
for r in rows:
    print(r[0], r[1])
# commit the changes

conn.commit()
# close the database connection
conn.close()