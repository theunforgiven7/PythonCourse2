import sqlite3
from sqlite3 import connect


def create_database(database: str) -> None:
    conn = sqlite3.connect(database + '.sqlite')
    conn.close()


database: str = input("Надайте назву для нової бази даних: ")
create_database(database)

with connect(database) as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS "Table_1" (
        "id"	INTEGER,
        "name"	TEXT,
        "num"	INTEGER,
        "date"	TEXT,
        "big_num"	INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT)
)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS "Table_2" (
        "id"	INTEGER,
        "name"	TEXT UNIQUE,
        "num"	INTEGER,
        "date"	TEXT,
        "big_num"	INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT)
)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS "Table_3" (
        "id"	INTEGER,
        "name"	TEXT,
        "num"	INTEGER NOT NULL,
        "date"	TEXT,
        "big_num"	INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT)
)''')

    con.commit()
