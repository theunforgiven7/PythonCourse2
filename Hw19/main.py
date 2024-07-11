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
            WHEN SUBSTR(Phone, 1, 2) IN ('+1') THEN 'North America'
            WHEN SUBSTR(Phone, 1, 3) IN ('+44', '+49', '+43', '+32',
            '+33', '+49', '+91', '+39', '+31',
            '+47', '+48', '+34', '+46', '+44') THEN 'Eurasia'
            WHEN SUBSTR(Phone, 1, 4) IN ('+353', '+358', '+351', '+453', '+420')
            THEN 'Eurasia'
            WHEN SUBSTR(Phone, 1, 3) IN ('+61') THEN 'Australia'
            WHEN SUBSTR(Phone, 1, 3) IN ('+54', '+55', '+56')
            THEN 'South America'
            ELSE 'Other'
        END AS ContinentCustomer,
        COUNT(CustomerId) AS "кількість покупців"
    FROM
        Customer
    GROUP BY
        ContinentCustomer
    ''')

    print(*cur.fetchall(), sep='\n')
