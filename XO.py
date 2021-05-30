import random

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

letters = 'ABC'
digits = '012'

def print_board(board):

    print('    A    B    C')
    for index, row in enumerate(board):
        print(f'{index} {row}')
print_board(board)

def player_move():

    move_incorrect = True
    while move_incorrect:
        move = input('Ваш хід (Велика літера + цифра, напр. C2): ')
        column = letters.index(move[0])
        row = int(move[1])
        if board[row][column] == ' ':
            board[row][column] = 'X'
            move_incorrect = False
        else:
            print("Клітинка зайнята")

def computer_move():

    move_incorrect = True
    while move_incorrect:
        letter = random.choice(letters)
        digit = random.choice(digits)
        column = letters.index(letter)
        row = int(digit)
        if board[row][column] == ' ':
            board[row][column] = 'O'
            move_incorrect = False

def is_board_full(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                return False
    return True

def is_player_win(symbol, board):

    for i in range(len(board)):
        win = True
        for j in range(len(board[i])):
            if board[i][j] != symbol:
                win = False
        if win:
            return True

    for j in range(len(board[0])):
        win = True
        for i in range(len(board)):
            if board[i][j] != symbol:
                win = False
        if win:
            return True

    win = True
    for i in range(len(board)):
        if board[i][i] != symbol:
            win = False
    if win:
        return True

    win = True
    for i in range(len(board)):
        if board[i][len(board) - 1 - i] != symbol:
            win = False
    if win:
        return True

def is_computer_win(symbol, board):

    for i in range(len(board)):
        win = True
        for j in range(len(board[i])):
            if board[i][j] != symbol:
                win = False
            if win:
                return True

def is_game_tie(board):

    return is_board_full(board) and not (is_player_win('X', board) or is_player_win('O', board))

def messages():

    if is_player_win('X', board):

        print()
        print("▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲")
        print("◀▶      P L A Y E R     (* ᴗ *)     W O N !      ◀▶")
        print("▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼")

        return is_player_win('X', board)

    if is_computer_win('O', board):

        print()
        print("▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲")
        print("◀▶      C O M P U T E R   (x ᴖ x)   W O N !      ◀▶")
        print("▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼")

        return is_computer_win('X', board) # WHY X ???

    if is_game_tie(borad):
        print('game tie')

def game_over(board):

    return is_player_win('X', board) or is_player_win('O', board) or is_board_full(board) #WHY O ???

def play():

    while True:
        player_move()
        print_board(board)
        if game_over(board):
            messages()
            break

        computer_move()
        print_board(board)
        if game_over(board):
            messages()
            break

play()