arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

top_right = 0
bottom_left = 0

top_left = 0
bottom_right = 0

# bottom_left

for i in range(len(arr)):
       for j in range(i+1):
              bottom_left += arr[i][j]

for i in range(len(arr)):
       for j in range(i, len(arr)):
              top_right += arr[i][j]

for i in range(len(arr)):
       for j in range(len(arr)-i):
              top_left += arr[i][j]

for i in range(len(arr)):
       for j in range(len(arr)-i-1, len(arr)):
              bottom_right += arr[i][j]

print('Bottom Right angle =', bottom_right)
print('Top Left angle =', top_left)
print('Top Right angle =', top_right)
print('Bottom Left angle =', bottom_left)
