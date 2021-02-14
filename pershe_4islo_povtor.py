arr = [7, 5, 2, 6, 8, 9, 1, 5, 2, 0, 1]

#  zystrilu = [7] << 5
#             [7, 5] << 2
#             [7, 5, 2] << 6
#             [7, 5, 2, 6] << 8
#             [7, 5, 2, 6, 8] << 9
#             [7, 5, 2, 6, 8, 9] << 1
#             [7, 5, 2, 6, 8, 9, 1] << 5
#             [7, 5, 2, 6, 8, 9, 1] <<<<< 5, break

arr_2 = []

for elem in arr:
	if elem in arr_2:
		print(elem)
		break
	arr_2.append(elem)

""" or set:
arr_2 = set()

for elem in arr:
	if elem in arr_2:
		print(elem)
		break
	arr_2.add(elem)
"""