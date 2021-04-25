arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

middle = 0
right = 0
left = 0

for i in range(len(arr)):
       for j in range(len(arr[i])):
              if i == j:
                     middle += arr[i][j]
              if i <= j:
                     right += arr[i][j]
              if j <= i:
                     left += arr[i][j]

print('Diagonal = ', middle)
print('Right angle =', right)
print('Left angle =', left)