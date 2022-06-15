import sqlite3

# Creating database
conn = sqlite3.connect('Baza_pyth')

c = conn.cursor()

# Create tables
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
	langauage VARCHAR(64)
	) ''')

conn.commit()

