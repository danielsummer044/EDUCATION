arr = [[-1, -1, 0], [0, -1, 0], [-1, 0, 0]]

i = 1
for row in range(len(arr)):
    for col in range(len(arr[row])):
        if arr[row][col] == 0:
            arr[row][col] = i
            i += 1
print(arr)