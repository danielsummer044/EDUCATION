mas = [-4, -1, 9, 5, -3, 1, 2, 0, 6]

minimal = 0
maximum = 0

for i in range(len(mas)):

	if mas[i] < minimal:
		minimal = mas[i]

	if mas[i] > maximum:
		maximum = mas[i]

print("Min element of array:")
print(minimal)
print("Max element of array:")
print(maximum)

summ = minimal + maximum
print("Summ of min and max:")
print(summ)