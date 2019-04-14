import sqlite3
# sqlite3 database connection
conn = sqlite3.connect("new.db")
# get a cursor object used to execute SQL commands
cur = conn.cursor()
# create a dictionary of sql queries
sql = {'average': "SELECT avg(population) FROM population",
'maximum': "SELECT max(population) FROM population",
'minimum': "SELECT min(population) FROM population",
'sum': "SELECT sum(population) FROM population",
'count': "SELECT count(city) FROM population"}
# run each sql query item in the dictionary
for keys, values in sql.items():
# run sql
    cur.execute(values)
# fetchone() retrieves one record from the query
    result = cur.fetchone()
# output the result to screen
    print(keys + ":", result[0])