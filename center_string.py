"""
string = 'Hello World!'
space_width = '-' * 10
print(space_width + string + space_width)
"""

"""
string = 'Hello World!'
string_len = len(string)

width = 40
space = '-'
space_width = space * width

left_pos = (width // 2) - string_len
#center_pos = (width // 2) + 1
right_pos = (width // 2)

print(left_pos * space + string + right_pos * space )
#for i in range(center_pos, width + 1):
#    print(i)
"""

"""
string = 'Hello World!'
new_string = string.center(40, '-')
print(new_string)
"""

string = 'Hello World!'
width = 40
space = '-'
left_right = width - len(string)
left = left_right // 2
right = left
print(left * space + string + right * space)

