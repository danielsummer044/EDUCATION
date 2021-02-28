arr = [7, 12, 323, 14, 5, 113, 25, 7, 8, 10, 9, 36, 232]

def digits(number):

	counter = 0

	while number > 0:
		digit = number % 10
		counter += 1
		number = number // 10
		counter += 1
	return digit

n = 2
