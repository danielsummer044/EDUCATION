mas = [7, 1, 13, 4, 17, 12, 16, 18, 3, 6, 5, 7]

index_parne = 0
parne = False
for i in range(len(mas)):
	if mas[i] % 2 == 0:
		index_parne = i
		parne = True
	if parne == True:
		break

#print(index_parne)


index_neparne = 0
neparne = False
for i in range(len(mas)-1, 0, -1):
	if mas[i] % 2 != 0:
		index_neparne = i
		neparne = True
	if neparne == True:
		break

#print(index_neparne)


if index_parne < index_neparne:
	for i in range(index_parne+1, index_neparne):
		print(mas[i])
else:
	for i in range(index_neparne+1, index_parne):
		print(mas[i])