mas = [1, 22, -3, 4, 9, 7, -24]

"""
mas[0] = 0
mas[1] = 0
mas[3] = 0
mas[5] = 0 
mas[6] = 0
print(mas)
"""
#mas[2] = nothing 
#mas[4] = nothing

"""
for i in range(len(mas)):
	mas[i] = 0

	mas[2] = -3
	mas[4] = 9

print(mas)
"""


x = -3
y = 9

for i in range(len(mas)):
	if mas[i] == x or mas[i] == y:
		mas[i] != 0
	else:
		mas[i] = 0
print(mas)

