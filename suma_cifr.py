#a = [11, -23, 13, 45, 51, -96, 69, 71, 19, 54, 99]

a = 123

def suma_cifr(a):
	summ = 0
	while a > 0:
		cifra = a % 10
		a = a // 10
		summ += cifra
	return summ

print(suma_cifr(a))

"""
d = a % 10

a = a // 10
c = a % 10

a = a // 10
b = a % 10
"""


#summ = d + b + c
#print(summ)