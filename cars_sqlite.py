import sqlite3


def create_db():
	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	# Create table
	cursor.execute('''CREATE TABLE IF NOT EXISTS cars
	             (brand text, year int, price real)''')

	# Insert a row of data
	cursor.execute("INSERT INTO cars VALUES ('BMW', 2010, 20000), ('Opel', 2015, 15000), ('Audi', 2020, 25000), ('Mazda', 2019, 18000), ('Fiat', 2018, 19000)")
	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()
	print('success')


# TODO: uncomment to create new db
# create_db()

def search_cars_by_year(year):
	""" Serch all cars younger than year. """
	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	cars = cursor.execute("SELECT brand, year FROM cars WHERE year >= ?", (year,)).fetchall()
	print(cars)

	conn.close()


def sort_cars_by_price(order='ASC'):
	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	if order == 'ASC':
		query = "SELECT * FROM cars ORDER BY price ASC"
	else:
		query = "SELECT * FROM cars ORDER BY price DESC"
	

	cars = cursor.execute(query).fetchall()
	print(cars)

	conn.close()


def sort_cars_by_year(order='ASC'):
	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	query = "SELECT * FROM cars ORDER BY year %s" % order
	
	cars = cursor.execute(query).fetchall()
	print(cars)


# search_cars_by_year(2018)

def search_cars_by_price(price_1, price_2):
	""" Serch all cars younger than year. """
	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	cars = cursor.execute("SELECT brand, year, price FROM cars WHERE price >= ? AND price <= ? ORDER BY price ASC", (price_1, price_2)).fetchall()
	print(cars)

	conn.close()


sort_cars_by_price()
sort_cars_by_year()

search_cars_by_price(18000, 20000)