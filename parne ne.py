n = 15
for i in range(1, n+1):
	if i % 3 == 0 and i % 5 == 0:
		print("Fizz Buzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)



"""
for i in range(1, 11):
	parnist = 'neparne'
	if i % 2 == 0:
		parnist = 'parne'


	print("%s %s" % (i, parnist))
"""

"""
i = 1
print("%s %s" % (i, "ne parne"))
i = 2
print("%s %s" % (i, "parne"))
i = 3
print("%s %s" % (i, "ne parne"))
i = 4
print("%s %s" % (i, "parne"))
i = 5
print("%s %s" % (i, "ne parne"))
"""