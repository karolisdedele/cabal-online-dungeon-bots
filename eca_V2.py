import time
from datetime import datetime
import pyautogui as pgui
import pydirectinput as pyd

a_skill = '3'  # bm3 a skill
b_skill = '0'  # bm3 b skill


# everything untill wave 1 to 3 is the same, seems to be fine, might update in the future

# -nf means needs fixing, just a reminder for myself cus I have goldfish memory sry

def enter_entry():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    while pgui.locateOnScreen('entry.png', confidence=0.8) is not None:
        x, y, z, k = pgui.locateOnScreen('entry.png', confidence=0.8)
        x += 100
        y += 100
        pyd.moveTo(x - 100, y - 100, 1)
        pyd.click(x, y)
        time.sleep(1)
        if pgui.locateOnScreen('cannot_enter.png', confidence=0.8) is not None:
            print("cant enter, no entries or no runs left")
            time.sleep(600)
            x1, y1, t, y = pgui.locateOnScreen('cannot_enter.png', confidence=0.8)
            pyd.click(x1, y1)
        elif pgui.locateOnScreen('check_entry_window.png', confidence=0.8) is not None:
            break


def entry_btn():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    while True:
        if pgui.locateOnScreen('enter_btn.png', confidence=0.9) is not None:
            x, y, z, k = pgui.locateOnScreen('enter_btn.png', confidence=0.9)
            pyd.click(x, y)
            break


def challenge_btn():
    pyd.PAUSE = 0.1
    pgui.PAUSE = 0.1
    while True:
        if pgui.locateOnScreen('challenge.png', confidence=0.9) is not None:
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
    pyd.press("7")
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
        pyd.press('z')
        if pgui.locateOnScreen('gate_dead.png', confidence=0.90, grayscale=True, region=(770, 30, 1115, 70)) is None:
            print("gate killed")
            break
        elif pgui.locateOnScreen('dungeon_failed.png', confidence=0.90, grayscale=True,
                                 region=(800, 370, 970, 400)) is not None:
            pyd.click(960, 730)
            time.sleep(1)
            pyd.moveTo(193, 126)
            time.sleep(0.2)
            pyd.moveTo(194, 126, 0.3)
            time.sleep(0.2)
            pyd.rightClick(204, 126)
            time.sleep(0.2)
            break
        else:
            pyd.press('z')
            pyd.press('0')
            pyd.press('4')
            pyd.press('5')
            pyd.press('6')


def retarget():
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    if pgui.locateOnScreen('retarget.png', confidence=0.95, grayscale=True, region=(770, 30, 1115, 70)) is None:
        pyd.press('z')


# Simple macro for waves 1 to 3. While it doesn't find lycs name, spams skills


"""def waves_1_to_3():
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    retarget()
    while pgui.locateOnScreen('Lycanus_name.png', confidence=0.95,
     grayscale=True,region=(770, 30, 1115,70)) is None:
        if pgui.locateOnScreen('dungeon_failed.png', confidence=0.90,
         grayscale=True, region=(800, 370, 970, 400)) is not None:
            pyd.click(960, 730)
            time.sleep(1)
            pyd.moveTo(193, 126)
            time.sleep(0.2)
            pyd.moveTo(194, 126, 0.3)
            time.sleep(0.2)
            pyd.rightClick(204, 126)
            time.sleep(0.2)
            run_bot()
            break
        else:
            retarget()
            pyd.press("4")
            pyd.press('9')
            pyd.press("5")
            pyd.press("6")
            pyd.press("0")
            pyd.press("7")
            pyd.press("8")
            pyd.press("=")"""


def waves_1_to_6():
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    retarget()
    while pgui.locateOnScreen('Leth_name.png', confidence=0.95, grayscale=True, region=(770, 30, 1115, 70)) is None:
        if pgui.locateOnScreen('dungeon_failed.png', confidence=0.90, grayscale=True,
                               region=(800, 370, 970, 400)) is not None:
            pyd.click(960, 730)
            time.sleep(1)
            pyd.moveTo(193, 126)
            time.sleep(0.2)
            pyd.moveTo(194, 126, 0.3)
            time.sleep(0.2)
            pyd.rightClick(204, 126)
            time.sleep(0.2)
            run_bot()
            break
        else:
            retarget()
            pyd.press("4")
            pyd.press('9')
            pyd.press("5")
            pyd.press("6")
            pyd.press("0")
            pyd.press("7")
            pyd.press("8")
            pyd.press("=")


# Needed for my weak ass cus I run ou of time kekW, can easly delete this and use wave_1_to_3 function untill tyrant


"""def lycanus_battle():
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    retarget()
    time.sleep(2)
    pyd.rightClick(1150, 950)
    while True:
        retarget()
        pyd.press(b_skill)
        if pgui.locateOnScreen('spataus_name.png', confidence=0.95, grayscale=True, 
        region=(770, 30, 1115,70)) is not None or \
                pgui.locateOnScreen('minotaur_name.png', confidence=0.95, 
                grayscale=True,region=(770, 30, 1115,70)) is not None:
            break
        else:
            pyd.press('-')
            pyd.press(b_skill)
            pyd.press("8")
            pyd.press('9')
            pyd.press('=')
            pyd.keyDown(b_skill)
"""

""" Does what the function says"""

"""def waves_4_to_6():
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    while True:
        retarget()
        if pgui.locateOnScreen('Leth_name.png', confidence=0.95, grayscale=True, region=(770, 30, 1115,70)) is not None:
            # looks for leth name to reuse ario and debuff leth
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
            pyd.press("0")
            pyd.press("7")
            pyd.press("8")
            pyd.press("=")"""


def leth_1st_form():  # macro for leth, spams bm3 a skill kek
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    time.sleep(2)
    pyd.rightClick(1170, 950)
    pyd.press('z')
    pyd.press('-')
    pyd.press('-')
    time.sleep(1.9)
    pyd.keyDown('alt')
    time.sleep(0.5)
    pyd.press("8")
    time.sleep(0.5)
    pyd.press("8")
    time.sleep(0.5)
    pyd.keyUp('alt')
    time.sleep(0.1)
    retarget()
    while True:
        pyd.press('z')
        pyd.press(a_skill)
        if pgui.locateOnScreen('Leth_2nd_form.png', confidence=0.95, grayscale=True,
                               region=(770, 30, 1115, 70)) is not None:  # checks if 2nd form has spawned
            break
        else:
            pyd.press('-')
            pyd.press(a_skill)
            pyd.press("8")
            pyd.press('9')
            pyd.press('=')
            pyd.press(a_skill)


def leth_2nd_form():  # macro for 2nd form, extends+uses sp pot cus my weak ass runs out of sp
    ext_time = 0
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    retarget()
    while True:
        ext_time += 1
        if ext_time == 20:
            pyd.keyDown('alt')
            time.sleep(0.3)
            pyd.press('=')
            pyd.press('9')
            time.sleep(1)
            pyd.press('=')
            pyd.press('9')
            pyd.press('=')
            time.sleep(1.1)
            pyd.keyUp('alt')
        elif pgui.locateOnScreen('Wave_over2.png', confidence=0.95,
                                 grayscale=True, region=(240, 30, 670, 130)) is not None:
            # cancels bm on wave over sometimes faks up but np
            pyd.PAUSE = 0.001
            pgui.PAUSE = 0.001
            print("found bm cancel condition - tyrant dead")
            pyd.moveTo(193, 126)
            time.sleep(0.2)
            pyd.moveTo(194, 126, 0.3)
            time.sleep(0.2)
            pyd.rightClick(204, 126)
            time.sleep(0.2)
            break
        elif pgui.locateOnScreen('dungeon_failed.png', confidence=0.85, grayscale=False) is not None:
            # checks if dung fails - working
            pyd.click(960, 730)
            time.sleep(1)
            pyd.moveTo(193, 126)
            time.sleep(0.2)
            pyd.moveTo(194, 126, 0.3)
            time.sleep(0.2)
            pyd.rightClick(204, 126)
            time.sleep(0.2)
            run_bot()
            break
        else:
            pyd.press('4')
            pyd.press("5")
            pyd.press("6")
            pyd.press("7")
            pyd.press(b_skill)
            pyd.press("8")
            pyd.press('9')
            pyd.press('=')
            pyd.press(b_skill)


def waves_7_to_9_macro():  # normal bm3 macro for later waves - kinda slow, needs adjustment, -nf
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    retarget()
    pyd.keyDown('alt')
    time.sleep(0.3)
    pyd.press('-')
    pyd.press('-')
    pyd.press('-')
    time.sleep(0.3)
    pyd.keyUp('alt')
    pyd.press(b_skill)
    if pgui.locateOnScreen('Wave_over2.png', confidence=0.95, grayscale=True, region=(240, 30, 670, 130)) is not None:
        print("found bm cancel condition - wave(7,6 or 9) over")
        pyd.moveTo(193, 126)
        time.sleep(0.1)
        pyd.moveTo(194, 126, 0.3)
        time.sleep(0.1)
        pyd.rightClick(204, 126)
        time.sleep(0.1)
        pyd.press('8')
        time.sleep(31)
        return
    else:
        pyd.press(b_skill)
        pyd.press('9')
        pyd.press("8")
        pyd.press(b_skill)
        pyd.press('=')
        pyd.press('-')
        pyd.press(b_skill)


# SOMETIMES BMS AFTER EXITING - needs fixing -nf
def waves_7_to_9_wc():
    # checks for exit conditions, uses macro cus otherwise 1
    # funtion goes through too many checks and slows down between attacks
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    retarget()
    time.sleep(1)
    while True:
        retarget()
        pyd.press(b_skill)
        if pgui.locateOnScreen('dungeon_failed.png', confidence=0.9, grayscale=True) is not None:
            pyd.moveTo(980, 730)
            pyd.click(980, 730)
            time.sleep(1)
            pyd.moveTo(193, 126)
            time.sleep(0.2)
            pyd.moveTo(194, 126, 0.3)
            time.sleep(0.2)
            pyd.rightClick(204, 126)
            time.sleep(0.2)
            break
        elif pgui.locateOnScreen('eins.png', confidence=0.95, grayscale=True) is not None:
            pyd.moveTo(1855, 155)
            pyd.click(1854, 155)
            time.sleep(0.5)
            pyd.click(960, 600)
            pyd.moveTo(195, 125)
            pyd.rightClick(196, 124)
            break
        else:
            waves_7_to_9_macro()


def bot_sequence():  # calls every function in the needed order + writes to log file - ok 9652
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
    time.sleep(0.5)
    path_from_turn()
    waves_1_to_6()
    leth_1st_form()
    leth_2nd_form()
    print("leth 2nd form")
    waves_7_to_9_wc()
    print("till the end")
    time.sleep(1)
    now = datetime.now()
    file = open('Run_log.txt', "a")  # creates a file named run_log.txt
    current_time = now.strftime("%H:%M:%S")  # checks current time on your pc
    current_date = now.strftime("%B %d, %Y")
    print("Run finished at =", current_time)  # prints when the run was finished in console
    file.write("Run finished at: ")  # writes when you finished the run in log file
    file.write(str(current_date))
    file.write("\n")  # adds new line
    file.write(str(current_time))
    file.write("\n")  # adds new line
    file.close()
    pyd.moveTo(760, 400, 1)  # dun even remember why I added this


time.sleep(2)


def run_bot():
    runs_done = 0
    while True:
        file = open('Run_log.txt', "a")  # opens log file
        runs_done += 1
        bot_sequence()
        print("Runs done: ", runs_done)  # prints in console the run count
        file.write("Runs done: ")  # writes in log file how many runs you have done
        file.write(str(runs_done))  # adds the run count
        file.write('\n')  # adds a new line so logs arent messy or hard to read
        file.close()


# self explanatory rly
time.sleep(0)
run_bot()
