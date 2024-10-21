import numpy as np
import random
import json

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

def smart_move(board, player, computer, move_all, first, data_win, data_fail):
    # 先把优先级最高的必走子求出来
    board_copy = board.copy()
    available_move = get_available_move(board)
    for letter in [computer, player]:
        for move in available_move:
            make_move(board_copy, letter, move)
            if game_won(board_copy, letter):
                return move
            make_move(board_copy, ' ', move)

    # 先手
    if first == 'computer':
        # 这是可执行的行动
        may = []
        # 当已经有机会必杀时
        for m in data_win:
            if move_all == m['position'][:len(move_all)]:
                model_player = m['model'][len(move_all)+1::2]
                # 这里不需要验证model_player是否为空，因为满足第一个if且不符合前面那段，就代表其不会为空
                if model_player.count(0) == 0:
                    may.append(m['position'])
        if may:
            move = random.choice(may)[len(move_all)]
            return move

        # 避免必输手的出现
        may_fail = []
        for m in data_fail:
            if move_all == m['position'][:len(move_all)]:
                model_player = m['model'][len(move_all)+2::2]
                if model_player.count(0) == 0:
                    may_fail.append(m['position'][len(move_all)])
        if may_fail:
            available_move = [j for j in available_move if j not in may_fail]

        # 无必走棋则预测下一步
        for m in data_win:
            if move_all == m['position'][:len(move_all)]:
                model_player = m['model'][len(move_all)+3::2]
                if model_player.count(0) == 0:
                    may.append(m['position'])
        if may:
            move_1 = []
            for m in may:
                move_1.append(m[len(move_all)])
            move_1 = [list(t) for t in set(tuple(_) for _ in move_1)]
            move_2 = []
            move_may = []
            final = 0
            for x in move_1:
                move_2.clear()
                for y in may:
                    if y[len(move_all)] == x:
                        move_2.append(y[len(move_all)+1])
                length = len([list(t) for t in set(tuple(_) for _ in move_2)])
                # 因为有if may:所以不需要再验证length是否为0，因为不可能为0
                if length > final:
                    final = length
                    move_may = [x]
                elif length == final:
                    move_may.append(x)

            may = [j for j in move_may if j in available_move]
            if may:
                move = random.choice(may)
                return move

    # 后手
    else:
        # 这是可执行的行动
        may = []
        # 当已经有机会必杀时
        for m in data_fail:
            if move_all == m['position'][:len(move_all)]:
                model_player = m['model'][len(move_all) + 1::2]
                # 这里不需要验证model_player是否为空，因为满足第一个if且不符合前面那段，就代表其不会为空
                if model_player.count(0) == 0:
                    may.append(m['position'])
        if may:
            move = random.choice(may)[len(move_all)]
            return move

        # 避免必输手的出现
        may_fail = []
        for m in data_win:
            if move_all == m['position'][:len(move_all)]:
                model_player = m['model'][len(move_all) + 2::2]
                if model_player.count(0) == 0:
                    may_fail.append(m['position'][len(move_all)])
        if may_fail:
            available_move = [j for j in available_move if j not in may_fail]

        # 无必走棋则预测下一步
        for m in data_fail:
            if move_all == m['position'][:len(move_all)]:
                model_player = m['model'][len(move_all) + 3::2]
                if model_player.count(0) == 0:
                    may.append(m['position'])
        if may:
            move_1 = []
            for m in may:
                move_1.append(m[len(move_all)])
            move_1 = [list(t) for t in set(tuple(_) for _ in move_1)]
            move_2 = []
            move_may = []
            final = 0
            for x in move_1:
                move_2.clear()
                for y in may:
                    if y[len(move_all)] == x:
                        move_2.append(y[len(move_all) + 1])
                length = len([list(t) for t in set(tuple(_) for _ in move_2)])
                # 因为有if may:所以不需要再验证length是否为0，因为不可能为0
                if length > final:
                    final = length
                    move_may = [x]
                elif length == final:
                    move_may.append(x)

            may = [j for j in move_may if j in available_move]
            if may:
                move = random.choice(may)
                return move

    move = random.choice(available_move)
    return move


def get_player_move(board, letter, move_all):
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
    move_all.append(move)

def tictactoe(size=3):
    print('Welcome Tictactoe game')
    player, computer = get_player_selection()
    print(f'Your selection is {player}, and computer\'s is {computer}')
    turn = who_go_first()
    # 这个参数是给smart_move传参用的
    first = turn
    print(f'{turn} go first')
    board = generate_board(size)

    move_all = []

    file_win = open('D:/python_work/train/数据结构/井字棋/win.txt', 'r', encoding='UTF-8')
    data_win = json.loads(file_win.read())
    file_win.close()

    file_fail = open('D:/python_work/train/数据结构/井字棋/fail.txt', 'r', encoding='UTF-8')
    data_fail = json.loads(file_fail.read())
    file_fail.close()

    while get_available_move(board):
        if turn == 'player':
            get_player_move(board, player, move_all)
            print(board)
            if game_won(board, player):
                print("Congrats, you won")
                return
            turn = 'computer'
        else:
            print('computer move')
            move = smart_move(board, player, computer, move_all, first, data_win, data_fail)
            make_move(board, computer, move)
            move_all.append(move)
            print(board)
            if game_won(board, computer):
                print('Computer won')
                return
            turn = 'player'
    print('Game is tie')

if __name__ == '__main__':
    tictactoe(3)