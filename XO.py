board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

letters = 'ABC'

def print_board(board):
    print('   A     B    C')
    for index, row in enumerate(board):
        print(f'{index} {row}')

print_board(board)

move = input('Ваш хід: ')
column = letters.index(move[0])
row = int(move[1])

board[row][column] = 'X'

print_board(board)
