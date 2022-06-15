import sqlite3
import json

# Creating database
conn = sqlite3.connect('Baza_pyth')

c = conn.cursor()

# Wyświetlić klientów którzy mieszkają kod zamieszkania 52-856
c.execute('''SELECT JSON_OBJECT(
	'id', id,
	'name', name,
	'last_name', last_name,
	'zip_code', zip_code
	)
	FROM client WHERE zip_code LIKE '52-856' ''')

output = c.fetchall()
print(output)

# Wyświetlić adres pod którym mieszka Patryk Nowak
c.execute('''SELECT JSON_OBJECT(
	'id', id,
	'country', country,
	'city', city,
	'street', street,
	'number', number,
	'zip_code', zip_code)
	FROM address WHERE zip_code IN 
	(SELECT zip_code FROM client WHERE name LIKE 'Patryk' AND last_name LIKE 'Nowak') ''')

output = c.fetchall()
print(output)

# Wyświetlić film z kategorii thriller w języku angielskim
c.execute('''SELECT JSON_OBJECT(
	'id', id,
	'name', name,
	'category', category,
	'length', length,
	'language', language)
	FROM film WHERE category LIKE 'Thriller' AND language LIKE 'english' ''')

output = c.fetchall()
print(output)

# Zmień długość i język filmu o id=2 zgodnie z tabelą
c.execute('''UPDATE film SET  language = 'polish', length = 97 WHERE id = 2''')

#Usuń film o id=1
c.execute('''DELETE FROM film WHERE id = 1 ''')

conn.commit()

