"""
mas = [1, 4, 5, 8, 3, 6, 7, 2, 11, 9]
for i in range(len(mas)):
	x = mas[i]
	y = mas[i+2]
	z = x + y
	if z == 8:
		print(z)
"""

mas = [1, 4, 5, 8, 3, 6, 7, 2, 11, 9]
summ = []
for i in range(1, len(mas)-1):
	left = mas[i-1]
	right = mas[i+1]
	if left + right == mas[i]:
		summ.append(mas[i])

print(summ)