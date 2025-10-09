import sqlite3

coon = sqlite3.connect("database.db")
cur = coon.cursor()
tovar = cur.execute('select * from avto').fetchall()
print(tovar)