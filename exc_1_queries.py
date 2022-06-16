import sqlite3


def queries(c):
    c.execute('''SELECT JSON_OBJECT(
        'id', id,
        'name', name,
        'last_name', last_name,
        'zip_code', zip_code
        )
        FROM client WHERE zip_code LIKE '52-856' ''')
    print(c.fetchall())

    c.execute('''SELECT JSON_OBJECT(
        'id', id,
        'country', country,
        'city', city,
        'street', street,
        'number', number,
        'zip_code', zip_code)
        FROM address WHERE zip_code IN
            (SELECT zip_code FROM client WHERE
             name LIKE 'Patryk' AND last_name LIKE 'Nowak') ''')
    print(c.fetchall())

    c.execute('''SELECT JSON_OBJECT(
        'id', id,
        'name', name,
        'category', category,
        'length', length,
        'language', language)
        FROM film WHERE category LIKE 'Thriller' AND language LIKE 'english' ''')
    print(c.fetchall())


def modify(c, conn):
    c.execute('''UPDATE film SET  language = 'polish', length = 97 WHERE id = 2''')
    c.execute('''DELETE FROM film WHERE id = 1 ''')
    conn.commit()


def main():
    conn = sqlite3.connect('Baza_pyth')
    c = conn.cursor()
    queries(c)
    
    modify(c, conn)


if __name__ == "__main__":
    main()
