import pydirectinput as pyd
import pyautogui as pgui
import time

def buy_medal():
    time.sleep(1)
    pyd.keyDown('alt')
    pyd.click(304,249)
    pyd.keyUp('alt')
    pyd.click(912,475)
    pyd.typewrite('55')
    pyd.click(965,650)
    time.sleep(0.5)
    pyd.keyDown('alt')
    pyd.click(304,249)
    pyd.keyUp('alt')
    pyd.click(912,475)
    pyd.typewrite('55')
    pyd.click(965,650)
    time.sleep(0.5)
    pyd.keyDown('alt')
    pyd.click(304,249)
    pyd.keyUp('alt')
    pyd.click(912,475)
    pyd.typewrite('55')
    pyd.click(965,650)
    time.sleep(0.5)
    pyd.keyDown('alt')
    pyd.click(304,249)
    pyd.keyUp('alt')
    pyd.click(912,475)
    pyd.typewrite('55')
    pyd.click(965,650)
    time.sleep(0.5)
    pyd.keyDown('alt')
    pyd.click(304,249)
    pyd.keyUp('alt')
    pyd.click(912,475)
    pyd.typewrite('55')
    pyd.click(965,650)

def sell_medal():
    pyd.keyDown('alt')
    pyd.click(1882,522)
    pyd.keyUp('alt')
    pyd.click(961,601)

def run():
    while True:
        buy_medal()
        time.sleep(0.5)
        sell_medal()

run()