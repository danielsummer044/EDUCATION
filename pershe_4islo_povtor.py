arr = [7, 5, 2, 6, 5, 2, 2, 5, 3, 1, 0]

for i in range(0, len(arr)-2):
	if arr[i+2] == arr[i-1]:
		print(arr[i-1])
