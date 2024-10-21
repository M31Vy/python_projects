# tictactoe - 为a-study需要的smart_move_1函数做的专供版（同时也是中间版）。
import numpy as np
import random

def generate_board(size, value=' '):
    return np.full((size, size), value)

def get_player_selection():
    letter = ''
    while letter not in ['X', 'O']:
        letter = input('Do you want to be X or O?').upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_go_first():
    x = random.randint(0,1)
    if x:
        return 'computer'
    else:
        return 'player'

def make_move(board, letter, position):
    board[position[0], position[1]] = letter

def row_won(board, letter):
    h, w = board.shape
    for y in range(h):
        ans = True
        for x in range(w):
            if board[y, x] != letter:
                ans = False
                break
        if ans:
            return ans
    return False

def column_won(board, letter):
    h, w = board.shape
    for y in range(w):
        ans = True
        for x in range(h):
            if board[x, y] != letter:
                ans = False
                break
        if ans:
            return ans
    return False

def diag_won(board, letter):
    h, w = board.shape
    ans = True
    for y in range(h):
        if board[y, h-y-1] != letter:
            ans = False
            break
    if ans:
        return ans

    ans = True
    for x in range(w):
        if board[x, x] != letter:
            ans = False
            break
    if ans:
        return ans
    return False

def game_won(board, letter):
    return row_won(board, letter) \
        or column_won(board, letter) \
        or diag_won(board, letter)

def get_available_move(board):
    move = []
    h, w = board.shape
    for y in range(h):
        for x in range(w):
            if board[y, x] == ' ':
                move.append([y, x])
    return move

def make_random_move(board, letter):
    available_move = get_available_move(board)
    move = random.choice(available_move)
    make_move(board, letter, move)

def smart_move_1(board, player, computer):
    board_copy = board.copy()
    available_move = get_available_move(board)
    for letter in [computer, player]:
        for move in available_move:
            make_move(board_copy, letter, move)
            if game_won(board_copy, letter):
                return move
            make_move(board_copy, ' ', move)
    return None

def smart_move(board, player, computer):
    move = smart_move_1(board, player, computer)
    if move:
        # 靠这里更新一下走棋来避免结果出bug，或许就可以不用copy棋盘了,但这样的话上一个函数就不好单独使用了。
        make_move(board, computer, move)
    else:
        make_random_move(board,computer)


def get_player_move(board, letter):
    h, w = board.shape
    move = [-1, -1]
    available_move = get_available_move(board)
    while move not in available_move:
        move = input(f'What is your move (0-{h-1}, 0-{w-1})?').split(',')
        try:
            move = [int(move[0]), int(move[1])]
        except:
            pass
    make_move(board, letter, move)

def tictactoe(size=3):
    print('Welcome Tictactoe game')
    player, computer = get_player_selection()
    print(f'Your selection is {player}, and computer\'s is {computer}')
    turn = who_go_first()
    print(f'{turn} go first')
    board = generate_board(size)
    while get_available_move(board):
        if turn == 'player':
            get_player_move(board, player)
            print(board)
            if game_won(board, player):
                print("Congrats, you won")
                return
            turn = 'computer'
            print('computer move')
        else:
            smart_move(board, player, computer)
            print(board)
            if game_won(board, computer):
                print('Computer won')
                return
            turn = 'player'
    print('Game is tie')

if __name__ == '__main__':
    tictactoe(3)