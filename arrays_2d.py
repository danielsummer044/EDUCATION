array = [[1,1,1,1],
         [1,2,2,2],
         [3,3,3,3]]

for i in range(len(array)):
    flag = True
    for j in range(len(array[i])-1):
        if array[i][j] != array[i][j+1]:
            flag = False
            break
    if flag:
        print(array[i])


"""
array1 = [2, 2, 2, 2]
array2 = [1, 2, 2, 2]
array3 = [1] + [2] * 100000000

def is_equal(arr):
    for i in range(len(arr) - 1):
        if arr[i] != arr[i+1]:
            return False
    return True

print(is_equal(array1))
print(is_equal(array2))
print(is_equal(array3))
"""


"""
array = [1, 2, 1, 1, 3, 3, 3, 5, 5, 5, 5]

count = 1
max_count = 1
elem = array[0]
subarray = [array[0]]
maxsubarray = [array[0]]

for i in range(len(array) - 1):
    if array[i] == array[i+1]:
        count += 1
        subarray.append(array[i])
    else:
        if count > max_count:
            max_count = count
            count = 1
            elem = array[i]
            maxsubarray = subarray[:]
        subarray = [array[i+1]]

    if count > max_count:
        max_count = count
        count = 1
        elem = array[i]
        maxsubarray = subarray[:]

print(f"max count: {max_count}")
print(f"elem: {elem}")
print(f"subarray: {[elem] * max_count}")
print(f"subarray: {maxsubarray}")
"""