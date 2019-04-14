# executemany() method

import sqlite3
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
   
# insert multiple records using a tuple
    cars = [
        ('Ford', 'Ford_01', 10),
        ('Ford', 'Ford_02', 20),
        ('Ford', 'Ford_03', 30),
        ('Honda', 'Honda_01', 40),
        ('Honda', 'Honda02', 50)
        ]

# insert data into table
    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)

# commit the changes
    c.commit()

# close the database connection
    c.close()