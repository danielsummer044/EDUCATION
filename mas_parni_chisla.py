N = 10

import random

mas = []
for i in range(N):
	mas.append(random.randint(1, 100))
	print(mas[i])

#mas = [1, 6, 8, 7, 3, 4, 10, 22, 9]
print('-------')
for i in range (len(mas)):
	if mas[i] % 2 == 0:
		print(mas[i])
