array = [30, 25, 5, -36, 100, 255]

for n in array:
    if n > 0 and n % 5 == 0 and n % 6 == 0 and n % 4 != 0:
        print(n)