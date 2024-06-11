from sqlite3 import connect


with connect('C:/Users/mariy/Downloads/Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()
    1
    cur.execute('''SELECT * FROM Customer
                                LIMIT 3''')
    print(*cur.fetchall(), sep ='\n')

    # 2
    cur.execute('''SELECT SUM(Total)
                                FROM Invoice''')
    print(*cur.fetchone())

    # 3
    cur.execute('''SELECT *
                            FROM Invoice
                            WHERE BillingCity == "Paris"''')
    print(*cur.fetchall(), sep ='\n')

    # 4
    cur.execute('''SELECT MIN(InvoiceDate)
                            FROM Invoice''')
    print(*cur.fetchone())

    # 5
    cur.execute('''SELECT MAX(InvoiceDate)
                            FROM Invoice''')
    print(*cur.fetchone())
