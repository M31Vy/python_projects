from func import *
import json

computer_1 = 'X'
computer_2 = 'O'
board = generate_board(3)
num = 0

win = []
fail = []
position = []
model = []


def select(num_x):
    if num_x % 2 == 0:
        return computer_1, computer_2
    else:
        return computer_2, computer_1

def smart(num_y, position_x,model_x):
    letter_1, letter_2 = select(num_y)
    num_y += 1
    # 注意这里是先看自己能不能赢，按照smart_move_1()的函数写法，letter_1得放后面
    move = smart_move_1(board, letter_2, letter_1)
    if move:
        make_move(board, letter_1, move)
        position_x.append(move)
        # 没得选就加个1
        model_x.append(1)

        if game_won(board, computer_1):
            # 先手胜利情况
            win.append({'position':position_x,'model':model_x})
        elif game_won(board, computer_2):
            # 后手胜利情况
            fail.append({'position':position_x,'model':model_x})
        elif get_available_move(board):
            # 在无胜利结果的情况下看还有没有下的地方
            smart(num_y,position_x[:],model_x[:])

        # 返回上一级前重置棋盘
        make_move(board, ' ', move)

    else:
        # 下面占个位，防止循环干扰。
        position_x.append(None)
        model_x.append(None)
        for m in get_available_move(board):
            make_move(board, letter_1, m)
            position_x.pop()
            position_x.append(m)
            # 可以选就加个0
            model_x.pop()
            model_x.append(0)

            if get_available_move(board):
                # 在无胜利结果的情况下看还有没有下的地方，因为这里是必定无胜利结果的，所以可以简化
                smart(num_y, position_x[:], model_x[:])

            # 返回上一级前重置棋盘
            make_move(board, ' ', m)

smart(num,position,model)

# 输出为json数据格式，并且按照无空格的方式输出
with open('D:/python_work/train/数据结构/井字棋/win.txt','w',encoding='UTF-8') as f_win:
    f_win.write(json.dumps(win, separators=(',',':')))

with open('D:/python_work/train/数据结构/井字棋/fail.txt','w',encoding='UTF-8') as f_fail:
    f_fail.write(json.dumps(fail, separators=(',',':')))