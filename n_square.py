n = 16
square = False

for i in range(1, n+1):
    m = i ** 2
    if m == n:
        square = True
        break
print(square)


"""
n = 10
for i in range(1, n+1):
    m = i ** 2
    sqrt = pow(m,1/2)
    #print(m)
    if m == sqrt:
        print(m)
"""

"""
n = 10
for i in range(1, n+1):
    m = i ** 2
    #print(m)
    if m % 2 == 0:
        print(m)
"""