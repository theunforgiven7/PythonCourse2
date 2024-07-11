from sqlite3 import connect


with connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()

    cur.execute('''SELECT *
                                FROM Customer
                                WHERE LENGHT(Company) == (SELECT MAX(LENGHT(Company)
                                FROM Customer
                                ''')
    print(*cur.fetchone(), sep=' ')

    cur.execute('''SELECT COUNT(*)
                                FROM Customer
                                WHERE Company is NULL AND Fax is NULL
                                ''')
    print(*cur.fetchone())


    cur.execute('''
    SELECT
        CASE
                WHEN Phone LIKE '+1%' THEN 'N America'
                WHEN Phone LIKE '+2%' THEN 'Africa'
                WHEN Phone LIKE '+5%' THEN 'Sou A'
                WHEN Phone LIKE '+3%' THEN 'Eur'
                WHEN Phone LIKE '+6%' THEN 'Aus'
                WHEN Phone LIKE '+8%' THEN 'Asia'
                ELSE "unknown"
            END AS Continent,
            COUNT (*),
        FROM Customer
        GROP BY Continent

    ''')

    print(*cur.fetchall(), sep='\n')
