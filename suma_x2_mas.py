mas = [[1,2,3],
       [4,5,6],
       [7,8,9]]

suma_mas = 0
for i in range(len(mas)):
	for j in range(len(mas[i])):
		suma_mas = suma_mas+ mas[i][j]
"""
s1 = mas[0][0] + mas[0][1] + mas[0][2]
s2 = mas[1][0] + mas[1][1] + mas[1][2] 
"""
print(suma_mas)