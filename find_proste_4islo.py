"""
a = 5
b = 1

if a / a == b and a / b == a:
	print('Proste')
"""

arr = [7, 9, 11, 41, 14, 81, 5, 3, 1, 2]

for i in range(len(arr)):
	if arr[i] / arr[i] == 1 and arr[i] / 1 == arr[i]:
		print('Proste')