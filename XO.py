import random


board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

letters = 'ABC'
digits = '012'

def print_board(board):
    print('   A     B    C')
    for index, row in enumerate(board):
        print(f'{index} {row}')

print_board(board)

def player_move():
    # Перевірити чи клітинка не зайнята
    move = input('Ваш хід (Велика літера + цифра, напр. C2): ')
    column = letters.index(move[0])
    row = int(move[1])
    board[row][column] = 'X'

def computer_move():
    # Перевірити чи клітинка не зайнята
    letter = random.choice(letters)
    digit = random.choice(digits)
    column = letters.index(letter)
    row = int(digit)
    board[row][column] = 'O'


def play():
    while True:
        player_move()
        computer_move()
        print_board(board)
        # break коли гра завершена
        break

play()