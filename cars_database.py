FILENAME='cars.csv'

def read_all_data(filename):

	f = open(filename, 'r')
	data = f.readlines()
	return data[1:]


def get_cars_less_than(cars_data, price):

	cars = []
	for car_info in cars_data:
		if int(car_info.split(';')[2]) < price:
			cars.append(car_info)
	return cars


def search_cars_by_year(cars_data, year):

	"""Search all newest cars, starting from given year"""

	cars = []
	for car_year in cars_data:
		if int(car_year.split(';')[1]) >= year:
			cars.append(car_year)
	return cars


def sort_cars(cars_data, order):

	""" order - ASC, DESC """

	for i in range(len(cars_data)):
		for j in range(len(cars_data)):
			if order == 'ASC':
				if int(cars_data[i].split(';')[2]) < int(cars_data[j].split(';')[2]):
					cars_data[i], cars_data[j] = cars_data[j], cars_data[i]
			else:
				if int(cars_data[i].split(';')[2]) > int(cars_data[j].split(';')[2]):
					cars_data[i], cars_data[j] = cars_data[j], cars_data[i]
	return cars_data






#DZ 1

def sort_cars_by_year(cars_data, year):

	for i in range(len(cars_data)):
		for j in range(len(cars_data)):

				if int(cars_data[i].split(';')[1]) < int(cars_data[j].split(';')[1]):
					cars_data[i], cars_data[j] = cars_data[j], cars_data[i]
	return cars_data




# DZ 3

import csv 

with open("cars.csv", "r") as csvfile:

	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)

with open("cars.csv", "a") as csvfile:

	fieldnames = ["Model (marka)", "year", "price"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writerow({"Model (marka)": "Kamaz", "year": 2002, "price": 6000})

exit()



def main():

	all_data = read_all_data(FILENAME)
	cars = get_cars_less_than(all_data, 20000)

	print(cars)

	cars = search_cars_by_year(all_data, 2019)

	print(cars)

	cars = sort_cars(all_data, 'DESC')
	print(cars)






# DZ 1

	cars_by_year = sort_cars_by_year(all_data, 2019)
	print(cars_by_year)


main()