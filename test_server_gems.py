import pydirectinput as pyd
import pyautogui as pgui
import time


#pgui.mouseInfo()

def buy_gems():
    time.sleep(0.5)
    pyd.keyDown('alt')
    time.sleep(0.5)
    pyd.click(30, 600)
    pyd.keyUp('alt')
    pyd.click(910, 475)
    pyd.typewrite('55')
    pyd.click(965, 650)
    time.sleep(1)



def use_gems():
    pyd.rightClick(1647, 244)#1
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1695,240)#2
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1735,237)#3
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1786,239)#4
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1831,241)  # 5
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1876,243)  # 6
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1558,290)  # 7
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1602,289)  # 8
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1651,291)  # 9
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1696,293)  # 10
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1740,287)  # 11
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1783,289)  # 12
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1833,292)  # 13
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1868,291)  # 14
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1556,337)  # 15
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1602,335)  # 16
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1647,336)  # 17
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1693,337)  # 18
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1741,338)  # 19
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1789,338)  # 20
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1833,336)  # 21
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1876,340)  # 22
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1556,384)  # 23
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1599,385)  # 24
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1653,382)  # 25
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1693,384)  # 26
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1743,385)  # 27
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1791,383)  # 28
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1830,383)  # 29
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1873,377)  # 30
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1554,424)  # 31
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1604,425)  # 32
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1604,425)  # 33
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1642,427)  # 34
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1695,427)  # 35
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1744,427)  # 36
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1786,429)  # 37
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1837,433)  # 38
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1877,430)  # 39
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1555,476)  # 40
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1597,475)  # 41
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1644,477)  # 42
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1694,477)  # 43
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1736,474)  # 44
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1790,470)  # 45
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1839,476)  # 46
    pyd.click(960, 600)
    time.sleep(0.3)
    pyd.rightClick(1868,477)  # 47
    pyd.click(960, 600)
    time.sleep(5)



def run_buyer():
    while True:
        buy_gems()
        use_gems()

time.sleep(3)
run_buyer()
