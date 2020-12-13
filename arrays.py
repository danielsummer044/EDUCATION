n = 7

mid = (n + 1) // 2
arr = []
#for i in range(1, mid+1):  # mid = 4, range(1, 5), 1,2,3,4
#    arr.append(i)

#for i in range(mid-1, 0, -1):
#	arr.append(i)

i = 1;
while i <= mid:
	arr.append(i) # arr = [], <- 1, arr[1] <-2, arr[1, 2]
	i = i + 1

i = mid - 1;
while i > 0:
	arr.append(i)
	i = i - 1

print(arr)