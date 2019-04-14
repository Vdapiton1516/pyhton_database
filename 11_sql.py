# JOINing data from multiple tables
import sqlite3

# sqlite3 database connection
conn = sqlite3.connect("new.db")
# get a cursor object used to execute SQL commands
cur = conn.cursor()
cur.execute("""SELECT DISTINCT population.city, population.population,
regions.region FROM population, regions WHERE
population.city = regions.city ORDER by population.city ASC""")
rows = cur.fetchall()
for r in rows:
    print("City: " + r[0])
    print("Population: " + str(r[1]))
    print("Region: " + r[2])
    print("")


# commit the changes

conn.commit()
# close the database connection
conn.close()