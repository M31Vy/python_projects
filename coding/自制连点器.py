import pyautogui
import time


def get_position():  # 打印当前鼠标坐标
        print("当前鼠标的坐标为：", pyautogui.position())  # 循环执行pyautogui.position()获取位置坐标

def autoclick(x,y):
    time.sleep(5)
    num_seconds = 3
    pyautogui.moveTo(x,y,duration=num_seconds) # 移过去的过程中用的秒数
    time.sleep(3)
    i = 1000
    while i:
        i -= 1
        time.sleep(0.5)
        pyautogui.click()

get_position()
autoclick(585,461)