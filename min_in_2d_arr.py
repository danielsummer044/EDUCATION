arr = [[2, 1, 3],
       [3, 5, 4],
       [9, 8, 7]]

minimal = [0][0]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < minimal:
            minimal = arr[i][j]
        print(minimal)