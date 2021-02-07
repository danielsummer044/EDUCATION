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
for i in range(len(mas)):
	l = mas[i]
	r = mas[i+2]
	if l + r == 8:
		x = summ.append(l)
		print(x)