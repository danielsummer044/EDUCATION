arr = [[1, 2, 3, 11],
       [4, 5, 6, 12],
       [7, 8, 9, 13]]

#       3, 2, 1
#       6, 5, 4
#       9, 8, 7

# swap columns`
for element in arr:

    last_element_id = len(element) - 1
    temp = element[0]
    element[0] = element[last_element_id]
    element[last_element_id] = temp

print(arr)

# swap lines
temp = arr[0]
arr[0] = arr[len(arr)-1]
arr[len(arr)-1] = temp
print(arr)