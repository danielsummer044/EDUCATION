
#Upper
"""
n = 9
for i in range(n):
	print(" " * (n - i) + "*" * (i * 2 - 1))
"""

#Lower
"""
n = 9
for i in range(0,5):
    print(' ' * i + '*' * (n - i * 2) + '' * i)
"""

#Sand timer
"""
def lower(n):
	n = 9
	for i in range(0,5):
		print(' ' * i + '*' * (n - i * 2) + '' * i)
	return n

def upper(n):
	n = 9
	for i in range(2,6):
		print(" " * (n - i - 4) + "*" * (i * 2 - 1))
	return n
lower(9)
upper(9)
"""