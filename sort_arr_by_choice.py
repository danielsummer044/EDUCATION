arr = [78, 12, 1, 34, 123, 321, 12, 35]

# 1 , min = 1, arr = [1, 14, 78, 34, 123, 321, 12, 34]
# 2, min of arr[1:] = 12, arr = [1, 12, 78, 34, 123, 321, 14, 34]
# 3, min of arr[2:] = 14 , arr =  [1, 12, 14, 34, 123, 321, 78, 34]
# ...
# len(arr), min arr[len(arr):]

for i in range(len(arr)):
    # 0, 1, 2, 3, ... кожен раз потрібно шукати мінімум серед решти елементів

    minimal = arr[i]
    index_min = i

    for j in range(i, len(arr)):
        # пошук мінімального
        if arr[j] < minimal:
            minimal = arr[j]
            index_min = j

    # swap elements
    arr[i], arr[index_min] = arr[index_min], arr[i]

print(arr)