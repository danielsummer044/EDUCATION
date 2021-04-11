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



def game_tie(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X" or board[i][j] == "O":
                count += 1
                if count == 9:
                    print("THE GAME ENDS IN A TIE!")
                    return True
                return False


def messages():

    if is_player_win():
        print("PLAYER WON!")
    if is_computer_win():
        print("COMPUTER WON!")



def game_over(board):

    return is_player_win('X', board) or is_player_win('O', board) or is_board_full(board)



def play():

    while True:
        player_move()
        print_board(board)
        if game_over(board):
            break

        computer_move()
        print_board(board)
        if game_over(board):
            break



play()