"""
arr = [121, 258, 457, 321, 423, 701, 308, 307, 306]
summ = 0

for i in range(len(arr)):

	l = arr[i] % 10
	m = (arr[i] // 10) % 10
	f = (arr[i] // 10) // 10
	summ = l + m + f
	if summ < 10:
		print(arr[i])
"""

def suma_cifr(chislo):
	suma = 0
	while chislo > 0:
		cifra = chislo % 10
		suma = suma + cifra
		chislo = chislo // 10
	return suma


arr = [121, 258, 457, 321, 423, 701, 308, 307, 306, 1111, 404, 2021, 3001, 10101010]

for i in range(len(arr)):
	summ = suma_cifr(arr[i])
	if summ < 10:
		print(arr[i])