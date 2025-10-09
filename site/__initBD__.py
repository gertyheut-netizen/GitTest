
import sqlite3

coon = sqlite3.connect("database.db")

coon.execute('''CREATE TABLE 'avto' (
	'id'	INTEGER UNIQUE,
	'name'	TEXT,
	'specifications'	TEXT,
	'mane'	INTEGER,
	PRIMARY KEY('id' AUTOINCREMENT)
);''') # запросы к бд

coon.execute('''CREATE TABLE "zakazy" (
	"id"	INTEGER,
	"name_user"	TEXT,
	"email"	TEXT,
	"number"	TEXT,
	"text"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);''') # запросы к бд

coon.commit()# записать изменения
coon.close()# закрывает БД