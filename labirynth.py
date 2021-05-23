from pprint import pprint

"""
. # # . . # #
. . # . . # #
# . . . . # .
# . # . . . #
# . . # . . #
# . # . # . #
# . . . # . .
"""

lab = """\
. # # . . # #
. . # . . # #
# . . . . # .
# . # . . . #
# . . # . . #
# . # . # . #
# . . . # . ."""

array = []
for row in lab.split('\n'):
   array.append(row.split())
pprint(array)

# -------------------
step = 1
array[0][0] = step
pprint(array)
m = len(array)
n = len(array[0])
while array[m-1][n-1] == '.':
    new_step = False
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == step:
                if i > 0:
                    if array[i-1][j] == '.':
                        array[i-1][j] = step + 1
                        new_step = True
                if j > 0:
                    if array[i][j-1] == '.':
                        array[i][j-1] = step + 1
                        new_step = True
                if i < len(array)-1:
                    if array[i+1][j] == '.':
                        array[i+1][j] = step + 1
                        new_step = True
                if j < len(array[i])-1:
                    if array[i][j+1] == '.':
                        array[i][j+1] = step + 1
                        new_step = True
    if not new_step:
        print('No exit')
        break
    step += 1


pprint(array)

a[0][0], a[1][0], a[1][1], a[m][n]

"""
start = array[0][0]
end = array[m][n]
step = 1  -> array[0][0]

[2][3]
array[i][j]

array[i-1][j]
array[i][j-1]
array[i+1][j]
array[i][j+1]
"""