mas = [[6, 34, -11, 43], [24, 66, 41, 32, -75]]

minmal_1 = mas[0][0]
minmal_2 = mas[1][0]



for i in range(len(mas)):
	for j in range(len(mas[i])): # ??????????????????????????

		if minmal_1 > mas[0][i]: # 2nd ?
			minmal_1 = mas[0][i]

		print(minmal_1)
