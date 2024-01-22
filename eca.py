import pyautogui as pgui
import pydirectinput as pyd
import time
from datetime import datetime


def enter_entry():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    while pgui.locateOnScreen('entry.png', confidence=0.8) != None:
        x, y, z, k = pgui.locateOnScreen('entry.png', confidence=0.8)
        x += 300
        y += 300
        pyd.moveTo(x - 100, y - 100, 1)
        pyd.click(x, y)
        if pgui.locateOnScreen('check_entry_window.png', confidence=0.8) != None:
            break


def entry_btn():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    while True:
        if pgui.locateOnScreen('enter_btn.png', confidence=0.9) != None:
            x, y, z, k = pgui.locateOnScreen('enter_btn.png', confidence=0.9)
            pyd.click(x, y)
            break


def challenge_btn():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    while True:
        if pgui.locateOnScreen('challenge.png', confidence=0.9) != None:
            x, y, z, k = pgui.locateOnScreen('challenge.png', confidence=0.9)
            pyd.click(x + 5, y + 5)
            break


def use_ario():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    pyd.keyDown("alt")
    time.sleep(0.5)
    pyd.press("8")
    time.sleep(0.5)
    pyd.keyUp("alt")
    time.sleep(0.5)
    return


def reuse_ario():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    pyd.keyDown("alt")
    time.sleep(0.2)
    pyd.press("8")
    time.sleep(0.5)
    pyd.press("8")
    pyd.keyUp("alt")
    return


def turn_screen_on_entry():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    pyd.moveTo(985, 205, 0.1)
    pyd.mouseDown(button="right")
    pyd.moveTo(605, 205, 0.1)
    pyd.mouseUp(button="right")
    use_ario()
    pyd.moveTo(995, 205, 0.1)
    return


def path_to_gate():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    pyd.moveTo(1020, 205, 0.1)
    pyd.press('1')
    time.sleep(0.5)
    pyd.press('2')
    time.sleep(0.5)
    pyd.press('1')
    time.sleep(0.5)
    pyd.press('2')
    time.sleep(0.5)
    pyd.press('1')
    time.sleep(0.5)
    pyd.press('2')
    time.sleep(0.5)
    pyd.moveTo(980, 253, 0.1)
    return


def turn_screen_on_turn():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    pyd.moveTo(985, 205, 0.1)
    pyd.mouseDown(button="right")
    pyd.moveTo(675, 205, 0.1)
    pyd.mouseUp(button="right")
    return


def path_from_turn():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    pyd.moveTo(1020, 205, 0.1)
    pyd.press('1')
    time.sleep(0.5)
    pyd.press('2')
    time.sleep(0.5)
    pyd.press('1')
    time.sleep(0.5)
    pyd.press('2')
    time.sleep(0.5)
    pyd.press('1')
    time.sleep(0.5)
    pyd.moveTo(1020, 253, 0.1)
    return


def hit_gate():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    while True:
        pyd.press('`')
        time.sleep(0.5)
        if pgui.locateOnScreen('gate_dead.png', confidence=0.55,grayscale=True) == None:
            print("gate killed")
            break
        else:
            pyd.press('`')
            pyd.press('4')
            pyd.press('5')
            pyd.press('6')


def retarget():
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    if pgui.locateOnScreen('retarget.png', confidence=0.95, grayscale=True) == None:
        pyd.press('`')
        pyd.press("0")


"""    if pgui.locateOnScreen('leth_spawned.png', confidence=0.95, grayscale=True) != None:
        return"""


def hit_macro():
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    while True:
        retarget()
        if pgui.locateOnScreen('Leth_name.png', confidence= 0.95, grayscale=True)!= None:
            pyd.keyDown("alt")
            time.sleep(0.5)
            pyd.press("8")
            time.sleep(0.5)
            pyd.press("8")
            time.sleep(0.5)
            pyd.press('2')
            time.sleep(0.7)
            pyd.press('1')
            pyd.keyUp("alt")
            break
        else:
            pyd.press("4")
            pyd.press('9')
            pyd.press("5")
            pyd.press("6")
            pyd.press("7")
            pyd.press("8")
            pyd.press("=")
            """if pgui.locateOnScreen('lyc_name.png', confidence=0.95, grayscale=True):
                pyd.keyDown('alt')
                pyd.press("1")
                pyd.press('2')
                pyd.keyUp('alt')
                continue"""
            """if pgui.locateOnScreen('Orc_mage.png', confidence=0.95, grayscale=True) != None or pgui.locateOnScreen(
                    'Orc_fighter.png', confidence=0.95, grayscale=True) != None:
                break"""



def bm3_synergies():
    if pgui.locateOnScreen('Wave_over.png', confidence=0.95, grayscale=True) != None:
        pyd.PAUSE = 0.001
        pgui.PAUSE = 0.001
        print("found bm cancel condition - wave over")
        pyd.moveTo(193, 126)
        time.sleep(0.2)
        pyd.moveTo(194, 126, 0.3)
        time.sleep(0.2)
        pyd.rightClick(204, 126)
        time.sleep(0.2)
        pyd.press('8')
        time.sleep(31)
    else:
        pyd.PAUSE = 0.001
        pgui.PAUSE = 0.001
        pyd.press("0")
        pyd.press('-')
        pyd.press("0")
        pyd.press('9')
        pyd.press('8')
        pyd.press("0")
        pyd.press("=")


def leth_macro():
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    while True:
        retarget()
        if pgui.locateOnScreen('leth_name.png', confidence=0.95, grayscale=True) != None:
            print("found - wave 6 completed. exiting")
            pyd.moveTo(1835, 156)
            pyd.click(1835, 156)
            time.sleep(0.5)
            pyd.click(960, 600)
            break
        else:
            bm3_synergies()


def run_bot():
        time.sleep(1)
        enter_entry()
        time.sleep(1.1)
        entry_btn()
        time.sleep(1.1)
        challenge_btn()
        time.sleep(0.5)
        turn_screen_on_entry()
        path_to_gate()
        turn_screen_on_turn()
        path_from_turn()
        hit_gate()
        time.sleep(1)
        path_from_turn()
        hit_macro()
        leth_macro()
        time.sleep(1)
        now = datetime.now()
        file = open('Run_log.txt', "a")
        current_time = now.strftime("%H:%M:%S")
        print("Tun finished at =", current_time)
        file.write("Run finished at: ")
        file.write(str(current_time))
        file.write("\n")
        pyd.moveTo(760, 400, 1)



time.sleep(2)
runs_done = 0
while True:
    file = open('Run_log.txt', "a")
    runs_done += 1
    run_bot()
    print("Runs done: ", runs_done)
    file.write("Runs done: ")
    file.write(str(runs_done))
    file.write('\n')