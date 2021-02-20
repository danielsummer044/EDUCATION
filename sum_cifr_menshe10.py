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

arr = [121, 258, 457, 321, 423, 701, 308, 307, 306, 1111, 404, 2021, 3001]

for i in range(len(arr)):

	d_4 = arr[i] % 10
	d_3 = (arr[i] // 10) % 10
	d_2 = (arr[i] // 100) % 10
	d_1 = arr[i] // 1000

	summ = d_4 + d_3 + d_2 + d_1
	if summ < 10:
		print(arr[i])