mas0 = [1001, 1010101, 10101110]

"""
mas = str(mas0)

x = mas.split("0")
for i in range(len(mas)):
	if mas[i] == "1":	# False True, continue ???
		print(mas[i], end = "")
print()
"""



def one(mas0):

	mas = str(mas0)	#from list to string
	x = mas.split("0")	#remove 0
	for i in range(len(mas)):
		if mas[i] == "1":
			print(mas[i], end = "")
	return
print(one(mas0))