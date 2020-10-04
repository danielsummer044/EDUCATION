mas = [-1, 6, 8, 2, 4, 3, 9, 0, 5, 1]
# mas = [1,2,3]
summ = 0

for i in range (0, len(mas)):
	summ = summ + mas[i]

print("Sum of elements in array: ")
print(summ)

n = len(mas)

print("Amount of elements: ")
print(n)

avg = summ / n

print("Average of array: ")
print(avg)


# find closest to avg
min_deviation = abs(mas[0] - avg)
closest = mas[0]

for i in range (1, len(mas)):
	deviation = abs(mas[i] - avg)
	if min_deviation > deviation:
		min_deviation = deviation
		closest = mas[i]
	
print(f"closest to avg: {closest}")