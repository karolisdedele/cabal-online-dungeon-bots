import pyautogui as pgui
import pydirectinput as pyd
import time
time.sleep(2)

while True:
    if pgui.locateOnScreen('medal_pot.png', confidence=0.8, grayscale=True) != None:
        x,y,z,k =pgui.locateOnScreen('medal_pot.png', confidence=0.8, grayscale=True)
        pyd.click(x+600,y)
        time.sleep(0.7)
        pyd.click(966, 606)
        time.sleep(0.6)
        pyd.click(1556,606)
        time.sleep(0.7)

    else:
        pyd.click(1323,784)
        time.sleep(1.3)
        pyd.click(966,606)
        time.sleep(1.3)
