# Program swaps max and min elements of an array

mas = [5, 6, 7, 4, 3, 2, 1, 0, -2, 0, 9, 4, 7, -5, 3, 1]


def find_max(array):
	maximum = array[0]
	for i in range(1, len(array)):
		if array[i] > maximum:
			maximum = array[i]
	return maximum


def find_min(array):
	maximum = array[0]
	for i in range(1, len(array)):
		if array[i] < maximum:
			maximum = array[i]
	return maximum


max_va = mas.index(find_max(mas))
min_va = mas.index(find_min(mas))

mas[max_va], mas[min_va] = mas[min_va], mas[max_va]
print(mas)