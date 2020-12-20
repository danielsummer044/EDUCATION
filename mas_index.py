mas = [4,3,2,1,3,7,3,9]

position = 0
minimal = mas[position]
min_index = position

for i in range(position, len(mas)):
	#print(f'index: {i}, elem: {mas[i]}')
	if minimal > mas[i]:
		min_index = i
		minimal = mas[min_index]

mas[position], mas[min_index] = mas[min_index], mas[position]

print(mas)

# next min
position = position + 1
minimal = mas[position]
min_index = position


for i in range(position, len(mas)):
	#print(f'index: {i}, elem: {mas[i]}')
	if minimal > mas[i]:
		min_index = i
		minimal = mas[min_index]

mas[position], mas[min_index] = mas[min_index], mas[position]

print(mas)

# next min
position = position + 1
minimal = mas[position]
min_index = position


for i in range(position, len(mas)):
	#print(f'index: {i}, elem: {mas[i]}')
	if minimal > mas[i]:
		min_index = i
		minimal = mas[min_index]

mas[position], mas[min_index] = mas[min_index], mas[position]

print(mas)

# next min
position = position + 1
minimal = mas[position]
min_index = position


for i in range(position, len(mas)):
	#print(f'index: {i}, elem: {mas[i]}')
	if minimal > mas[i]:
		min_index = i
		minimal = mas[min_index]

mas[position], mas[min_index] = mas[min_index], mas[position]

print(mas)
# next min
position = position + 1
minimal = mas[position]
min_index = position


for i in range(position, len(mas)):
	#print(f'index: {i}, elem: {mas[i]}')
	if minimal > mas[i]:
		min_index = i
		minimal = mas[min_index]

mas[position], mas[min_index] = mas[min_index], mas[position]

print(mas)
# next min
position = position + 1
minimal = mas[position]
min_index = position


for i in range(position, len(mas)):
	#print(f'index: {i}, elem: {mas[i]}')
	if minimal > mas[i]:
		min_index = i
		minimal = mas[min_index]

mas[position], mas[min_index] = mas[min_index], mas[position]

print(mas)
# next min
position = position + 1
minimal = mas[position]
min_index = position


for i in range(position, len(mas)):
	#print(f'index: {i}, elem: {mas[i]}')
	if minimal > mas[i]:
		min_index = i
		minimal = mas[min_index]

mas[position], mas[min_index] = mas[min_index], mas[position]

print(mas)
# next min
position = position + 1
minimal = mas[position]
min_index = position


for i in range(position, len(mas)):
	#print(f'index: {i}, elem: {mas[i]}')
	if minimal > mas[i]:
		min_index = i
		minimal = mas[min_index]

mas[position], mas[min_index] = mas[min_index], mas[position]

print(mas)