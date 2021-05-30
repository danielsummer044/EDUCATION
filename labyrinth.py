from pprint import pprint

def display_array(_array):
    for _y in range(0, h):
        line = ''
        for _x in range(0, w):
            _str = str(_array[_y][_x])
            if len(_str) == 1:
                _str += '  '
            elif len(_str) == 2:
                _str += ' '
            line += _str
        print(line)

lab_txt = open('labyrinth.txt', 'r', encoding='utf-8-sig')
labyrinth = lab_txt.read()
lab_txt.close()

h = len(labyrinth.split('\n')) - 1
w = len(labyrinth.split('\n')[0])

array = []

for i in range(0, h):
    temp_array = []
    for j in range(0, w):
        temp_array.append('⬜')
    array.append(temp_array)

splited = labyrinth.split('\n')

for y in range(0, h):
    for x in range(0, w):
        char = splited[y][x]
        if char == '⬛':
            array[y][x] = '⬛'

start_end = splited[h].split('|')
start = start_end[0].split(",")
start = [int(start[0]), int(start[1])]
end = start_end[1].split(",")
end = [int(end[0]), int(end[1])]

print(f'Start: ({start[0]}, {start[1]})')
print(f'End: ({end[0]}, {end[1]})')

step = 1
array[start[1]][start[0]] = step
m = len(array)
n = len(array[0])

while array[end[0]][end[1]] == '⬜':
    new_step = False
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == step:
                if i > 0:
                    if array[i-1][j] == '⬜':
                        array[i-1][j] = step + 1
                        new_step = True
                if j > 0:
                    if array[i][j-1] == '⬜':
                        array[i][j-1] = step + 1
                        new_step = True
                if i < len(array)-1:
                    if array[i+1][j] == '⬜':
                        array[i+1][j] = step + 1
                        new_step = True
                if j < len(array[i])-1:
                    if array[i][j+1] == '⬜':
                        array[i][j+1] = step + 1
                        new_step = True
    if not new_step:
        print('No exit')
        break
    step += 1


display_array(array)