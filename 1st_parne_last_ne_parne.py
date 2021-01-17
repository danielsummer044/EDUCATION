mas = [7, 1, 13, 4, 17, 12, 16, 18, 3, 6, 5]

parne = 0
for i in range(len(mas)):
	while parne == 1:
		mas[i] % 2 == 0
#print("parne")
print(mas[i])
"""
x = mas.index(mas[i])
print("Index of parne: ") # index of parne
print(x)
"""
"""
ne_parne = 0
for i in range(len(mas)):
	if mas[i] % 2 != 0:
		ne_parne = mas[i]
		#print(ne_parne)

mas2 = []
mas2.append(ne_parne)
#print(mas2[0])

y = mas2.index(ne_parne)
print("Index of ne parne: ")
print(y) # index of ne parne

z = 0
for i in range(len(mas)):
	if mas2[0] == mas[i]:
		z = mas[i]
		print(mas.index(z))
"""

mas = [5, 7, 1, 13, 4, 17, 12, 16, 18, 3, 6, 5, 7]
for i in range(mas[-1], mas[0]):
	mas[i] = 0
print(mas)