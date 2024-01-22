import time
import pyautogui as pgui
import pydirectinput as pyd

pgui.PAUSE = 0.001
pyd.PAUSE = 0.001


def enter_entry():
    coords = []
    while pgui.locateOnScreen('entry.png', confidence=0.8) is not None:
        coords.append(pgui.locateOnScreen('entry.png', confidence=0.8))
        pyd.moveTo(coords[0][0] + 100, coords[0][1] + 100, 1)
        pyd.click()
        time.sleep(1)
        coords.clear()
        if pgui.locateOnScreen('cannot_enter.png', confidence=0.8) is not None:
            print("cant enter, no entries or no runs left")
            time.sleep(300)
            coords.append(pgui.locateOnScreen('cannot_enter.png', confidence=0.8))
            pyd.click(coords[0][0], coords[0][1])
            coords.clear()
        elif pgui.locateOnScreen('check_entry_window.png', confidence=0.8) is not None:
            break


def entry_btn():
    while True:
        if pgui.locateOnScreen('enter_btn.png', confidence=0.9) is not None:
            x, y, z, k = pgui.locateOnScreen('enter_btn.png', confidence=0.9)
            pyd.click(x, y)
            break


def challenge_btn():
    while True:
        if pgui.locateOnScreen('challenge.png', confidence=0.9) is not None:
            x, y, z, k = pgui.locateOnScreen('challenge.png', confidence=0.9)
            pyd.click(x + 5, y + 5)
            break


def use_ario():
    pyd.keyDown("alt")
    time.sleep(0.5)
    pyd.press("8")
    time.sleep(0.5)
    pyd.press("7")
    time.sleep(0.5)
    pyd.keyUp("alt")
    time.sleep(0.5)
    return


def hit_gate():
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
    if pgui.locateOnScreen('retarget.png', confidence=0.95, grayscale=True, region=(770, 30, 1115, 70)) is None:
        pyd.press('z')


def wave_over():
    pyd.moveTo(193, 126)
    time.sleep(0.2)
    pyd.moveTo(194, 126, 0.3)
    time.sleep(0.2)
    pyd.rightClick(204, 126)
    time.sleep(1)
    pyd.keyDown('ctrl')
    time.sleep(0.1)
    pyd.press('1')
    time.sleep(0.1)
    pyd.keyUp('ctrl')


def travel_to_1st_wave_spot():
    pyd.PAUSE = 0.001
    pgui.PAUSE = 0.001
    pyd.moveTo(960, 70)
    time.sleep(0.1)
    pyd.moveTo(961, 71)
    time.sleep(0.1)
    pyd.press('1')
    time.sleep(0.6)
    pyd.press('2')
    time.sleep(0.6)
    pyd.press('1')
    time.sleep(0.6)
    pyd.press('2')
    pyd.moveTo(820, 120)
    time.sleep(0.1)
    pyd.moveTo(821, 121)
    time.sleep(0.6)
    pyd.press('1')
    time.sleep(0.6)
    pyd.press('2')
    time.sleep(0.6)
    pyd.press('1')
    time.sleep(0.6)
    pyd.press('2')
    time.sleep(0.6)
    pyd.moveTo(950, 200)
    time.sleep(0.1)
    pyd.moveTo(950, 201)
    time.sleep(0.6)
    pyd.press('1')
    time.sleep(0.6)
    pyd.press('2')
    time.sleep(0.6)
    pyd.press('1')
    time.sleep(0.6)


def travel_to_red_pillar():
    coords = []

    if pgui.locateOnScreen('red_pillar_name_transparent.png', confidence=0.7) is not None: # finds pillar name
        coords.append(pgui.locateOnScreen('red_pillar_name_transparent.png', confidence=0.7)) # adds coords to array
        pyd.moveTo(coords[0][0] + 200, coords[0][1] + 201) # moves mouse to found coords
        time.sleep(0.5)
        pyd.moveTo(coords[0][0] + 201, coords[0][1] + 200) # small offset so it doesn't mess up
        time.sleep(2)
        pyd.press('1') # dashes
        time.sleep(2)
        coords.clear() # clears array. NOTE: VERY IMPORTANT TO CLEAR IT
        time.sleep(2)
        coords.append(pgui.locateOnScreen('red_pillar_name_transparent.png', confidence=0.6))
        pyd.moveTo(coords[0][0] + 200, coords[0][1] + 201)
        time.sleep(0.5)
        pyd.moveTo(coords[0][0] + 201, coords[0][1] + 200)
        time.sleep(2)
        pyd.press('2')
        time.sleep(2)
        coords.clear()


def wave_1_macro():
    retarget()
    while True:
        retarget()
        pyd.press(['-', '3', '8', '=', '9', '0']) # skill usage sequence
        if pgui.locateOnScreen('wave_over.png', confidence=0.9) is not None:
            wave_over()
            break


def wave_2_macro():
    retarget()
    while True:
        retarget()
        pyd.press(['-', '3', '8', '=', '9', '0'])
        if pgui.locateOnScreen('wave_over.png', confidence=0.9) is not None:
            wave_over()
            break


def wave_3_macro():
    retarget()
    while True:
        retarget()
        pyd.press(['-', '3', '8', '=', '0'])
        if pgui.locateOnScreen('wave_over.png', confidence=0.9) is not None:
            wave_over()
            break


def travel_to_mage():  # travels to mage, needs slight adjustment cus char dashes on top of mage.
    pyd.moveTo(1450, 800)
    pyd.moveTo(1450, 801)
    pyd.press('1')
    time.sleep(0.6)
    pyd.press('2')
    time.sleep(0.6)


def mage_reposition():
    while True:
        if pgui.locateOnScreen('mage.png', confidence=0.9) is None: # looks for mage+hits so you dont die
            pyd.press('z')
            pyd.press(['-', '3', '8', '=', '0'])
        if pgui.locateOnScreen('mage.png', confidence=0.9) is not None: # once it finds mage, fades to the left so it's closer to golems
            pyd.moveTo(410, 500)
            print("reposition-mage")
            time.sleep(2)
            pyd.press('2')
            time.sleep(1)
            break


def kill_mage(): # does what it says
    print("killing mage")
    while True:
        if pgui.locateOnScreen('mage.png', confidence=0.8) is not None:
            pyd.press(['-', '3', '8', '=', '0'])
        else:
            print("mage killed")
            break


def go_to_golems():
    coords = []
    try: # tries looking for golems, should dash next to them if char did not wander off
        coords.append(pgui.locateOnScreen("golem_transparent.png", confidence=0.6))
        print("found golem")
        pyd.moveTo(coords[0][0] + 150, coords[0][1] + 301)
        pyd.moveTo(coords[0][0] + 151, coords[0][1] + 300)
        coords.clear()
        time.sleep(1)
        pyd.press('1')
        time.sleep(1)
        pyd.press('`')
        retarget()
        return
    except TypeError: #if it does not find golems, dashes to where they SHOULD BE
        print("golem wasnt found, dashing to top left")
        pyd.moveTo(500, 370)
        time.sleep(1)
        pyd.press('1')
        time.sleep(0.7)
        return


def detect_first_boss(): #looks for 1st boss
    while True:
        retarget()
        if pgui.locateOnScreen('freezer.png', confidence=0.8, grayscale=True) is not None:
            break


def first_boss_battle(): #attacks boss
    retarget()
    while True:
        pyd.press(['-', '3', '8', '=', '9', '0'])
        use_shorts()
        if pgui.locateOnScreen('wave_over.png', confidence=0.9) is not None:
            wave_over()
            time.sleep(2)
            retarget()
            pyd.press(['4', '5', '6','8'])
            break


def use_shorts(): #uses shorts when half hp, if you use shadowshield it slows down the hit macro but still hits
    if pgui.locateOnScreen("hp.png", confidence=0.95) is None:
        pyd.keyDown('alt')
        time.sleep(0.2)
        pyd.press(['1', '4', '9', '5', '5'])
        time.sleep(0.2)
        pyd.keyUp('alt')
        pyd.press(['-', '3', '8', '=', '9', '0'])
        return


def exit_conditions(): # some dumb stuff that needs testing
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
        return


def wave_4_macro():
    retarget()
    while True:
        retarget()
        pyd.press(['-', '3', '8', '=', '9', '0'])
        if pgui.locateOnScreen('wave_over.png', confidence=0.9) is not None:
            wave_over()
            break


def wave_5_macro():
    retarget()
    while True:
        retarget()
        exit_conditions()
        pyd.press(['-', '3', '8', '=', '9', '0'])
        if pgui.locateOnScreen('wave_over.png', confidence=0.9) is not None:
            wave_over()
            break


def wave_6_macro():
    retarget()
    while True:
        retarget()
        pyd.press(['-', '3', '8', '=', '9', '0'])
        exit_conditions()
        pyd.press(['-', '3', '8', '=', '9', '0'])
        if pgui.locateOnScreen('wave_over.png', confidence=0.9, grayscale=True) is not None:
            wave_over()
            break


def run_bot():
    time.sleep(1)
    enter_entry()
    time.sleep(0.5)
    entry_btn()
    time.sleep(0.5)
    challenge_btn()
    time.sleep(0.5)
    use_ario()
    time.sleep(0.5)
    hit_gate()
    time.sleep(0.5)
    travel_to_1st_wave_spot()
    time.sleep(10)
    wave_1_macro()
    time.sleep(1)
    travel_to_red_pillar()
    time.sleep(31)
    wave_2_macro()
    time.sleep(1)
    travel_to_red_pillar()
    time.sleep(1)
    travel_to_mage()
    time.sleep(1)
    time.sleep(26)
    mage_reposition()
    time.sleep(0.5)
    kill_mage()
    time.sleep(0.5)
    go_to_golems()
    time.sleep(1)
    wave_3_macro()
    time.sleep(1)
    travel_to_mage()
    time.sleep(28)
    first_boss_battle()
    travel_to_red_pillar()
    time.sleep(26)
    wave_4_macro()
    travel_to_red_pillar()
    time.sleep(25)
    wave_5_macro()
    travel_to_red_pillar()
    time.sleep(26)
    wave_6_macro()


while True:
    run_bot()
    time.sleep(1)
