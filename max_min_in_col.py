array = [[1, 2, 3, 10, 0],
         [4, 5, 6, 7, 1],
         [0, 8, 9, 6, 5]]


"""
min_elem = array[0][0]
max_elem = array[0][0]

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][0] < min_elem:
            min_elem = array[i][0]
        if array[i][0] > max_elem:
            max_elem = array[i][0]

print(min_elem)
print(max_elem)
"""

"""
min_elem = array[0][1]
max_elem = array[0][1]

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][1] < min_elem:
            min_elem = array[i][1]
        if array[i][1] > max_elem:
            max_elem = array[i][1]

print(min_elem)
print(max_elem)
"""

"""
min_elem = array[0][2]
max_elem = array[0][2]

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][2] < min_elem:
            min_elem = array[i][2]
        if array[i][2] > max_elem:
            max_elem = array[i][2]

print(min_elem)
print(max_elem)
"""

for i in range(len(array[0])):
    min_elem = array[0][i]
    max_elem = array[0][i]
    for j in range(len(array)):

        if array[j][i] < min_elem:
            min_elem = array[j][i]
        if array[j][i] > max_elem:
            max_elem = array[j][i]

    print("-" * 30)
    print("|", i+1, "col.", "|", "min :", min_elem, "|", "max :", max_elem, "|")
print("-" * 30)
