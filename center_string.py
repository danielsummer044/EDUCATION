"""
string = 'Hello World!'
space_width = '-' * 10
print(space_width + string + space_width)
"""

string = 'Hello World!'

width = 3
space = '-'
space_width = space * width

left_pos = (width // 2)
#center_pos = (width // 2) + 1
right_pos = (width // 2)

print(left_pos * space + string + right_pos * space )
#for i in range(center_pos, width + 1):
#    print(i)

