arr = [7, 12, 323, 14, 5, 113, 25, 7, 8, 10, 9, 36, 232]

def digits(number):

	amount_of_digits = 0
	print('-' * 20)
	while number > 0:
		number = number // 10
		amount_of_digits += 1
	print('-' * 20)
	return amount_of_digits

n = 2

for number in arr:
	if digits(number) == n:
		print(number)