mas = [1, 22, -3, 4, 9, 7, -24]

#mas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = 3, y = 7 => mas = [1, 2, 3, 0, 0, 0, 7, 8, 9, 10]
#mas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = 22
y = -24
index_of_x = mas.index(x)
index_of_y = mas.index(y)

if index_of_x < index_of_y:
	for i in range(index_of_x+1, index_of_y):
		mas[i] = 0

else:
	for i in range(index_of_y+1, index_of_x):
		mas[i] = 0

print(mas)
