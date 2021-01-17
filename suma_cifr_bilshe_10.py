"""Module designed to print number from list which has sum of digits > 10"""

def suma_cifr(a):
	summ = 0
	while a > 0:
		cifra = a % 10
		a = a // 10
		summ += cifra
	return summ


def main():
	a = [11, -23, 113, 45, 51, -96, 69, 71, 19, 54, 99]

	for number in a:  # for i in range(len(a)): number = a[i]
		if suma_cifr(number) > 10:
			print(number)


if __name__ == '__main__':
	main()
