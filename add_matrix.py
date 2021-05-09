
a = [[1, 2, 3, 4],
     [4, 5, 6, 7],
     [7, 8, 9, 0]]

b = [[3, 2, 1, 0],
     [6, 5, 4, 3],
     [9, 8, 7, 6]]

m = len(a)
n = len(a[0])

# HOMEWORK
def create_empty_array(m,n):
    c = [0] * n
    #? D:
    return c

print(create_empty_array(m,n))
# c = a + b => c[i][j] = a[i][j]+ b[i][j]
"""
for i in range(len(a)):
    for j in range(len(a[i])):
        c[i][j] = a[i][j] + b[i][j]
print(c)
"""