# Program prints elements of an array between min and max

mas = [5, 6, 7, 4, 3, 2, 1, 0, -2, 0, 9, 4, 7, -5, 3, 1]

minimal = mas[0]
maximum = mas[0]

min_index = 0
max_index = 0

for i in range(1, len(mas)):
	if mas[i] < minimal:
	   minimal = mas[i]
	   min_index = i
	if mas[i] > maximum:
	   maximum = mas[i]
	   max_index = i


# ----------
if min_index < max_index:
	for i in range(min_index+1, max_index):
		print(mas[i])
else:
	for i in range(max_index+1, min_index):
		print(mas[i])
