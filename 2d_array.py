arr = [[4, 5, 1],
       [6, 2, 3],
       [7, 9, 4]]

for i in range(len(arr)):

    maximum = arr[i][0]
    minimal = arr[i][0]

    for j in range(len(arr[i])):
        if arr[i][j] > maximum:
            maximum = arr[i][j]
        if arr[i][j] < minimal:
            minimal = arr[i][j]
    print('max:', maximum, 'min:', minimal)
