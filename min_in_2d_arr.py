arr = [[2, 1, 3],
       [3, 5, 4],
       [9, 8, 7]]

for i in range(len(arr)):
    minimal = arr[i][0]

    for j in range(len(arr[i])):
        if arr[i][j] < minimal:
            minimal = arr[i][j]

    print(minimal)
"""

arr = [5,3,1,4,2]

minimal = arr[0]

for i in range(len(arr)):
    if arr[i] < minimal:
        minimal = arr[i]

print(minimal)
"""

