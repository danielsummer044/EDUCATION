mas = [9, 5, 3, -1, 1, 2, 4, 7]

minimal = mas[0]
maximum = mas[0]

min_index = 0
max_index = 0

for i in range(1, len(mas)):
	if minimal > mas[i]:
		minimal = mas[i]
		min_index = i


for i in range(1, len(mas)):
	if maximum < mas[i]:
		maximum = mas[i]
		max_index = i

if max_index > min_index:
    left = min_index
    right = max_index
else:
	left = max_index
	right = min_index


for i in range (left+1, right):
	mas[i] = 0
	


#print(minimal)

#print(min_index)

#print(maximum)

#print(max_index)

print(mas)

