"""
a = 5
b = 1

if a / a == b and a / b == a:
	print('Proste')
"""

arr = [7, 9, 11, 41, 14, 81, 5, 3, 1, 2]

def is_proste(n):
	for dilnik in range(2, n):
		if n % dilnik == 0:
			return False
	return True



a = 5
print(f'{a} proste: {is_proste(a)}')


a = 6
print(f'{a} proste: {is_proste(a)}')

a = 12
print(f'{a} proste: {is_proste(a)}')

a = 13
print(f'{a} proste: {is_proste(a)}')

for number in arr:
	print(is_proste(number))