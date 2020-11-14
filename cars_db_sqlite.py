#----------------------------------------------------------------------------------------------------------------------------------------------------#

import sqlite3



def create_db():

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	# Create table
	cursor.execute('''CREATE TABLE IF NOT EXISTS cars (brand text, year int, price real)''')

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


# HOME WORK
#----------------------------------------------------------------------------------------------------------------------------------------------------#

def sort_by_brand(order):

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	if order == 'ASC':
		query = cursor.execute("SELECT * FROM cars ORDER BY brand ASC")
	else:
		query = cursor.execute("SELECT * FROM cars ORDER BY brand DESC")

	result = query.fetchall()
	conn.close()

	return result



def search_by_brand(brand):

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	query = cursor.execute("SELECT * FROM cars WHERE brand = ?", (brand)).fetchall()

	result = query.fetchall()
	conn.close()

	return result

#----------------------------------------------------------------------------------------------------------------------------------------------------#

def sort_by_year(order):

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	if order == 'ASC':
		query = cursor.execute("SELECT * FROM cars ORDER BY year ASC")
	else:
		query = cursor.execute("SELECT * FROM cars ORDER BY year DESC")

	result = query.fetchall()
	conn.close()

	return result



def search_by_year(year):

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	query = cursor.execute("SELECT year FROM cars WHERE year = ? ORDER BY year ASC", (year)).fetchall()

	conn.close()

	return result

#----------------------------------------------------------------------------------------------------------------------------------------------------#

def sort_by_price(order):

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	if order == 'ASC':
		query = cursor.execute("SELECT * FROM cars ORDER BY price ASC")
	else:
		query = cursor.execute("SELECT * FROM cars ORDER BY price DESC")

	result = query.fetchall()
	conn.close()

	return result



def search_by_price(price_1, price_2):

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	query = cursor.execute("SELECT price FROM cars WHERE price >= ? AND price <= ? ORDER BY price ASC", (price_1, price_2)).fetchall()

	result = query.fetchall()
	conn.close()

	return result

#----------------------------------------------------------------------------------------------------------------------------------------------------#
def main():

	cars = sort_by_price('ASC')
	print(cars)
	
main()