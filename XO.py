import random

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

letters = 'ABC'
digits = '012'

COMP_SYMBOL = 'O'

def print_board(board):
    """Друкує дошку з поставленими хрестиками та нуликами"""
    print('    A    B    C')
    for index, row in enumerate(board):
        print(f'{index} {row}')
print_board(board)

def player_move():
    """Питає гравця куди ставити хрестики і записує у масив"""
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
    """Симулює хід гравця, яким керує комп'ютер"""
    success = check_if_player_can_win(COMP_SYMBOL)
    if success:
        return

    success = check_if_player_can_win('X')
    if success:
        return

    move_incorrect = True
    while move_incorrect:
        letter = random.choice(letters)
        digit = random.choice(digits)
        column = letters.index(letter)
        row = int(digit)
        if board[row][column] == ' ':
            board[row][column] = COMP_SYMBOL
            move_incorrect = False

def check_if_player_can_win(symbol):
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == ' ':
            board[i][2] = COMP_SYMBOL
            return True
        if board[i][1] == symbol and board[i][2] == symbol and board[i][0] == ' ':
            board[i][0] = COMP_SYMBOL
            return True
        if board[i][0] == symbol and board[i][2] == symbol and board[i][1] == ' ':
            board[i][1] = COMP_SYMBOL
            return True

    for j in range(3):
        if board[0][j] == symbol and board[1][j] == symbol and board[2][j] == ' ':
            board[2][j] = COMP_SYMBOL
            return True
        if board[1][j] == symbol and board[2][j] == symbol and board[0][j] == ' ':
            board[0][j] = COMP_SYMBOL
            return True
        if board[0][j] == symbol and board[2][j] == symbol and board[1][j] == ' ':
            board[1][j] = COMP_SYMBOL
            return True

    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == ' ':
        board[2][2] = COMP_SYMBOL
        return True
    if board[1][1] == symbol and board[2][2] == symbol and board[0][0] == ' ':
        board[0][0] = COMP_SYMBOL
        return True
    if board[0][0] == symbol and board[2][2] == symbol and board[1][1] == ' ':
        board[1][1] = COMP_SYMBOL
        return True

    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == ' ':
        board[2][0] = COMP_SYMBOL
        return True
    if board[0][2] == symbol and board[2][0] == symbol and board[1][1] == ' ':
        board[1][1] = COMP_SYMBOL
        return True
    if board[2][0] == symbol and board[1][1] == symbol and board[0][2] == ' ':
        board[0][2] = COMP_SYMBOL
        return True
    return False

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


def game_tie(board):

    return is_board_full(board) and not (is_player_win('X', board) or is_player_win(COMP_SYMBOL, board))


def messages():

    if is_player_win('X', board):

        print()
        print("▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲")
        print("◀▶      P L A Y E R     (* ᴗ *)     W O N !      ◀▶")
        print("▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼")
        return None

    if is_player_win(COMP_SYMBOL, board):

        print()
        print("▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲")
        print("◀▶      C O M P U T E R   (x ᴖ x)   W O N !      ◀▶")
        print("▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼")
        return None


    print()
    print("▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲     ▼▲")
    print("◀▶                    GAME TIE!                  ◀▶")
    print("▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼     ▲▼")
    return None


def game_over(board):

    return is_player_win('X', board) or is_player_win(COMP_SYMBOL, board) or is_board_full(board) #WHY O ???

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