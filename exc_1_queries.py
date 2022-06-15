import sqlite3

# Creating database
conn = sqlite3.connect('Baza_pyth')

c = conn.cursor()

# Wyświetlić klientów którzy mieszkają kod zamieszkania 52-856
c.execute("SELECT * FROM client WHERE zip_code LIKE '52-856'")

output = c.fetchall()
for row in output:
	print(row)

# Wyświetlić adres pod którym mieszka Patryk Nowak
c.execute('''SELECT * FROM address WHERE zip_code IN 
	(SELECT zip_code FROM client WHERE name LIKE 'Patryk' AND last_name LIKE 'Nowak')
	''')

output = c.fetchall()
for row in output:
	print(row)

# Wyświetlić film z kategorii thriller w języku angielskim
c.execute("SELECT * FROM film WHERE category LIKE 'Thriller' AND language LIKE 'english'")

output = c.fetchall()
for row in output:
	print(row)