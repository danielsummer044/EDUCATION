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

	#Search all newest cars, starting from given year

	cars = []

	for car_year in cars_data:
		if int(car_year.split(';')[1]) >= year:
			cars.append(car_year)

	return cars



def sort_cars_by_brand_swap(cars_data, order):

	for i in range(len(cars_data)):
		for j in range(len(cars_data)):

			if order == 'ASC':
				if int(cars_data[i].split(';')[2]) < int(cars_data[j].split(';')[2]):
					cars_data[i], cars_data[j] = cars_data[j], cars_data[i]

			else:
				if int(cars_data[i].split(';')[2]) > int(cars_data[j].split(';')[2]):
					cars_data[i], cars_data[j] = cars_data[j], cars_data[i]

	return cars_data



# SORT CARS BY YEAR
def sort_cars_by_year(cars_data, order):

	for i in range(len(cars_data)):
		for j in range(len(cars_data)):

			if order == 'ASC':
					if int(cars_data[i].split(';')[1]) < int(cars_data[j].split(';')[1]):
						cars_data[i], cars_data[j] = cars_data[j], cars_data[i]

			else:
					if int(cars_data[i].split(';')[1]) > int(cars_data[j].split(';')[1]):
						cars_data[i], cars_data[j] = cars_data[j], cars_data[i]
		return cars_data



# ADD NEW CAR
import csv 

# ADD NEW CAR IN CSV FILE
with open(FILENAME, "a") as csvfile:
	dot = ";"
	fieldnames = ["brand", "year", "price"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writerow({"brand": "Kamaz", "year": 2002, "price": 6000})

# READ WITHOUT TXT FILE
with open(FILENAME, "r") as csvfile:

	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)

exit()



# MAIN
def main():

	all_data = read_all_data(FILENAME)

# PRINT CARS LESS THAN
	cars = get_cars_less_than(all_data, 20000)
	print(cars)

# PRINT CARS SEARCHED BY YEAR
	cars = search_cars_by_year(all_data, 2019)
	print(cars)

# PRINT CARS WITH SWAP NAME LIST
	cars = sort_cars_by_brand_swap(all_data, 'ASC')
	print(cars)

# PRINT CARS BY YEAR
	cars = sort_cars_by_year(all_data, 'DESC')
	print(cars)

main()