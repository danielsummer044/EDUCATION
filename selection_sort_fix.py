arr = [7, -1, 4, 12, 44, 76, 101, 6]

for i in range(len(arr)):
    minimal_index = i
    for j in range(i + 1, len(arr)):
        if arr[minimal_index] < arr[j]:
            minimal_index = j

    arr[i], arr[minimal_index] = arr[minimal_index], arr[i]
print(arr)