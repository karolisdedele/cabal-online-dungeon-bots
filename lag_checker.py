import time
import pydirectinput as pyd
import pyautogui as pgui
from timeit import default_timer as timer
from datetime import datetime


def lag_checker():
    time.sleep(2)
    start = timer()
    pyd.click(1580,750)
    pyd.click(1580,750)
    while pgui.locateOnScreen('rewards/lag_checker_login.png') is None:
        kekw = 0
    end = timer()
    total = end - start
    print(total)
    time.sleep(1)
    pyd.press("esc")
    now = datetime.now()
    file = open('Lag_log.txt', "a")  # creates a file named Lag_log.txt
    current_time = now.strftime("%H:%M:%S")  # checks current time on your pc
    file.write(str(current_time))
    file.write(" Login took: ")
    file.write(str(total))
    file.write("\n")  # adds new line
    file.close()


while True:
    lag_checker()