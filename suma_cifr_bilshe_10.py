a = [11, -23, 13, 45, 51, -96, 69, 71, 19, 54, 99]

summ = 0

for i in range(len(a)):

	cifra = a[i] % 10
	druga_cifra = a[i] // 10
	summ = cifra + druga_cifra

	if summ >= 10:
		print(summ)