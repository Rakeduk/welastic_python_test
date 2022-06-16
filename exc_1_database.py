import sqlite3


def create_tables(c, conn):
    c.execute('''CREATE TABLE IF NOT EXISTS client(
        id INTEGER,
        name VARCHAR(64),
        last_name VARCHAR(64),
        zip_code VARCHAR(6)
        ) ''')

    c.execute('''CREATE TABLE IF NOT EXISTS address(
        id INTEGER,
        country VARCHAR(64),
        city VARCHAR(64),
        street VARCHAR(64),
        number INTEGER,
        zip_code VARCHAR(6)
        ) ''')

    c.execute('''CREATE TABLE IF NOT EXISTS film(
        id INTEGER,
        name VARCHAR(255),
        category VARCHAR(64),
        length INTEGER,
        language VARCHAR(64)
        ) ''')
    conn.commit()


def insert_data(c, conn):
    c.execute('''INSERT INTO client VALUES
        (1, 'Patryk', 'Kowalski', '52-856'),
        (2, 'Maria', 'Kowalska', '52-856'),
        (3, 'Patryk', 'Nowak', '62-718')
        ''')

    c.execute(''' INSERT INTO address VALUES
        (1, 'Poland', 'Warszawa', 'Miejska', 26, '52-856'),
        (2, 'Poland', 'Poznań', 'Owcza', 75, '62-718')
        ''')

    c.execute('''INSERT INTO film VALUES
        (1, 'Inside Man', 'Thriller', 129, 'english'),
        (2, 'The Sandman', 'Horror', 112, 'english')
        ''')
    conn.commit()


def main():
    conn = sqlite3.connect('Baza_pyth')
    c = conn.cursor()
    create_tables(c, conn)
    insert_data(c, conn)

if __name__ == "__main__":
    main()
