from pprint import pprint
"""
board = '''\
8+-+-+-+-
7-+-+-+-+
6+-+-+-+-
5-+-+-+-+
4+-+-+-+-
3-+-+-+-+
2+-+-+-+-
1-+-+-+-+
 ABCDEFGH'''
"""
board = """\
+-+-+-+-
-+-+-+-+
+-+-+-+-
-+-+-+-+
+-+-+-+-
-+-+-+-+
+-+-+-+-
-+-+-+-+"""

#letters = 'ABCDEFGH'

arr = []
for row in board.split('\n'):
    arr.append(row)
#print(arr)

knight_start_pos = arr[0][6]
knight_end_pos = arr[2][5]

pprint(arr)