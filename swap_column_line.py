arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

#       3, 2, 1
#       6, 5, 4
#       9, 8, 7

for element in arr:

    last_element_id = len(element) - 1
    temp = element[0]
    element[0] = element[last_element_id]
    element[last_element_id] = temp

print(arr)