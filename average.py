mas = [-1, 6, 8, 2, 4, 3, 9, 0, 5, 1]
summ = 0

for i in range (1, len(mas)):
	summ = summ + mas[i]

print("Sum of elements in array: ")
print(summ)

n = len(mas)

print("Amount of elements: ")
print(n)

avg = summ / n

print("Average of array: ")
print(avg)



for i in range (1, len(mas)):
	if mas[i] == summ:
print(mas[i])