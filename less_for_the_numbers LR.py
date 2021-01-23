mas = [7, 3, 0, 9, 4, 11, 31, 8]

"""
for i in range(len(mas)):
	if mas[i] > mas[i+1]:
		print("Less for the numbers to the right: ", + mas[i])
	if mas[i] < mas[i+1]:
		print("Less for the numbers to the left: ", + mas[i])
"""

"""
for i in range(len(mas)):
	x = mas[i]
	y = mas[i+1]
	z = mas[i+2]
	if y < z or y > x:
		print(y)
"""


y = False
for i in range(len(mas)):
	x = mas[i]
	y = mas[i+1]
	z = mas[i+2]
	if y < z or y > x:
		print(y)
		y = True
		break
