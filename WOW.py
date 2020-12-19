mas = [1, 6, 8, 7, 3, 4, 10, 22, 9]
for i in range(len(mas)):
	for j in range(len(mas)):
		#1)x = mas[0] + mas[i]
		#2)x = mas[i] + mas[i] -- (mas[0] + mas[0], mas[1] + mas[1], mas[2] + mas[2])

		#      mas[i] + mas[j]
		#3)x = mas[0] + mas[1], mas[0] + mas[2], mas[0] + mas[3]

		#j = mas[0]
		"""
		if mas[0] != mas[i]:
			x = mas[0] + mas[i]
			print(x)

		if mas[1] != mas[i]:
			x = mas[1] + mas[i]
			print(x)

		if mas[2] != mas[i]:
			x = mas[2] + mas[i]
			print(x)
		"""

		
		if mas[j] != mas[i]:
				x = mas[j] + mas[i]
				if x > 10:
					print(x)
