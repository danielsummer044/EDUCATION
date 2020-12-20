mas = [[6, 34, -11, 43], [24, 66, 41, 32, -75]]

minmal_1 = mas[0][0]
maximal = mas[0][0]

for i in range(len(mas)):
	for j in range(len(mas[i])): # ??????????????????????????
		if minmal_1 > mas[i][j]: # 2nd ?
			minmal_1 = mas[i][j]

		if maximal < mas[i][j]: # 2nd ?
			maximal = mas[i][j]

print(minmal_1)
print(maximal)