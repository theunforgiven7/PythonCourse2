from sqlite3 import connect


with connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()

    cur.execute('''SELECT *, MAX(Company)
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
            WHEN Country IN ('Belgium', 'Czech Republic', 'Denmark',
            'Finland', 'France', 'Germany', 'Hungary', 'Ireland',
            'Italy', 'India', 'Netherlands', 'Norway', 'Poland', 'Portugal',
            'Spain', 'Sweden', 'United Kingdom', 'Australia', 'Austria')
            THEN 'Eurasia'
            WHEN Country IN ('Canada', 'USA') THEN 'North America'
            WHEN Country IN ('Argentina', 'Brazil', 'Chile') THEN 'South America'
            ELSE 'unknow'
        END AS ContinentCustomer,
        COUNT(CustomerId) AS "кількість покупців"
    FROM 
        Customer
    GROUP BY 
        ContinentCustomer
    ''')

    print(*cur.fetchall(), sep='\n')
