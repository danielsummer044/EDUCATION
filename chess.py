from pprint import pprint

cell = '□'
size = 8
knight = 'K'
letters = 'ABCDEFGH'
move = '*'

def print_board(board):
    # TODO: print_board
    pass


board = [[cell for i in range(size)] for j in range(size)]
pprint(board)

start_position = input('Введіть стартову позицію коня: ')

letter, digit = start_position
row = int(digit) - 1
col = letters.index(letter)
board[row][col] = knight

pprint(board)
print()

# TODO:
if row + 2 <= size -1 and col + 1 <= size - 1:
    board[row+2][col+1] = move
if row - 2 >= 0 and col - 1 >= 0:
    board[row-2][col-1] = move
if row - 1 >= 0 and col - 2 >= 0:
    board[row-1][col-2] = move

if row + 2 <= size - 1 and col - 1 >= 0:
    board[row+2][col-1] = move
if row + 1 <= size - 1 and col + 2 <= size - 1:
    board[row+1][col+2] = move

if row - 1 >= 0 and col + 2 <= size - 1:
    board[row-1][col+2] = move

if row + 1 <= size - 1 and col - 2 >= 0:
    board[row+1][col-2] = move

if row - 2 >= 0 and col - 1 >= 0:
    board[row-2][col-1] = move

pprint(board)

