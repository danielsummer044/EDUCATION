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

def sort_by_brand(order='ASC'):

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	if order == 'ASC':
		query = cursor.execute("SELECT * FROM cars ORDER BY brand ASC")
	else:
		query = cursor.execute("SELECT * FROM cars ORDER BY brand DESC")

	result = query.fetchall()
	conn.close()

	return result



def sort_by_year(order='ASC'):

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

	result = cursor.execute("SELECT * FROM cars WHERE year = ? ORDER BY year ASC", (year,)).fetchall()

	conn.close()

	return result



def sort_by_price(order='ASC'):

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	if order == 'ASC':
		query = cursor.execute("SELECT * FROM cars ORDER BY price ASC")
	else:
		query = cursor.execute("SELECT * FROM cars ORDER BY price DESC")

	result = query.fetchall()
	conn.close()



def search_by_price(price_1, price_2):

	conn = sqlite3.connect('cars.db')
	cursor = conn.cursor()

	query = cursor.execute("SELECT * FROM cars WHERE price >= ? AND price <= ? ORDER BY price ASC", (price_1, price_2)).fetchall()

	print(query)

	conn.close()



# MAIN
def main():

	
	"""
	# PRINT CARS LESS THAN
		cars = get_cars_less_than(all_data, 20000)
		print(cars)

	# PRINT CARS SEARCHED BY YEAR
		cars = search_cars_by_year(all_data, 2019)
		print(cars)

	# PRINT CARS WITH SWAP NAME LIST
		cars = sort_cars_by_brand_swap(all_data, 'ASC')
		print(cars)
	"""

    # PRINT CARS BY YEAR
	cars = search_by_price(15000, 18000)
	print(cars)

main()
