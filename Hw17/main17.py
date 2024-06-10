import sqlite3
from sqlite3 import connect


def create_database(database_name: str) -> None:
    conn = sqlite3.connect(database_name + '.sqlite3')
    conn.close()


database_name: str = input("Надайте назву для нової бази даних: ")
create_database(database_name)

with connect('C:/Users/mariy/Downloads/tes.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE "Table_1" (
        "id"	INTEGER,
        "name"	TEXT,
        "num"	INTEGER,
        "date"	INTEGER,
        "big_num"	INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT)
)''')

    cur.execute('''CREATE TABLE "Table_2" (
        "id"	INTEGER,
        "name"	TEXT UNIQUE,
        "num"	INTEGER,
        "date"	INTEGER,
        "big_num"	INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT)
)''')

    cur.execute('''CREATE TABLE "Table_3" (
        "id"	INTEGER,
        "name"	TEXT UNIQUE,
        "num"	INTEGER NOT NULL,
        "date"	INTEGER,
        "big_num"	INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT)
)''')
