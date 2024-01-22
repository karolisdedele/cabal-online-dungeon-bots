import time
import pyautogui
import pydirectinput as pyd
import pyautogui as pgui
from timeit import default_timer as timer

pyd.PAUSE = 0.001
pgui.PAUSE = 0.001
#item_1....4 coordinates for item slots in reward menu
item_1 = 961
item_2 = 1045
item_3 = 1126
item_4 = 1211
#set which item to take
row_item_1 = 0+ item_2 #takes 2nd item in row
row_item_2 = 1+ item_3
row_item_3 = 2+ item_4
row_item_4 = 3+ item_1
row_item_5 = 4+ item_1

lag_timer = 6

def lag_checker():
    time.sleep(1)
    ch_selector()
    ch_change_coords = [968, 600]
    pyd.click(ch_change_coords[0], ch_change_coords[1])
    time.sleep(1)
    start = timer()
    kekw = 0
    while pgui.locateOnScreen('rewards/lag_checker.png') is not None:
        kekw += 1
    end = timer()
    total = end - start
    print("timer: ",round(total,2))
    if float(total) >= lag_timer:
        return round(total,2)
    else:
        total==0
        time.sleep(2)
        lag_checker()


def item_selector():
    # opens and selects
    time.sleep(1)
    challenge_mission_button = []
    rewards_button = []
    challenge_mission_button.append(
        pgui.locateOnScreen('rewards/Challenge_mission_btn.png', region=(1507, 991, 1560, 1034))) #range =area near the button
    pyautogui.moveTo(challenge_mission_button[0])
    pyd.click()
    time.sleep(0.2)
    rewards_button.append(pgui.locateOnScreen('rewards/Reward_rank_btn.png'))
    pyautogui.moveTo(rewards_button[0])
    pyd.click()
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    time.sleep(1)
    row1.append(pgui.locateOnScreen('rewards/first_row_icon.png'))
    pyd.moveTo(row_item_1, row1[0][1])
    pyd.click()
    time.sleep(0.2)
    row2.append(pgui.locateOnScreen('rewards/second_row_icon.png'))
    pyd.moveTo(row_item_2, row2[0][1])
    pyd.click()
    time.sleep(0.2)
    row3.append(pgui.locateOnScreen('rewards/third_row_icon.png'))
    pyd.moveTo(row_item_3, row3[0][1])
    pyd.click()
    time.sleep(0.2)
    pgui.scroll(-1)
    row4.append(pgui.locateOnScreen('rewards/fourth_row_icon.png'))
    pyd.moveTo(row_item_4, row4[0][1])
    time.sleep(0.2)
    pyd.click()
    pgui.scroll(-1)
    row5.append(pgui.locateOnScreen('rewards/fifth_row_icon.png'))
    pyd.moveTo(row_item_5, row5[0][1])
    time.sleep(0.2)
    pyd.click()


def ch_selector():
    ch_btn = []
    time.sleep(0.5)
    pyd.press('o')
    ch_btn.append(pgui.locateOnScreen('rewards/ch_select-btn.png', region=(761, 383, 1070, 552))) #range = area near button
    pyd.moveTo(ch_btn[0][0], ch_btn[0][1])
    pyd.click()
    time.sleep(1)
    ch2 = []
    ch3 = []
    if pgui.locateOnScreen('rewards/current_ch2.png') is not None:
        ch3.append(pgui.locateOnScreen('rewards/ch3.png'))
        pyd.moveTo(ch3[0][0] + 100, ch3[0][1])
        pyd.click()
        pyd.click()
    elif pgui.locateOnScreen('rewards/current_ch3.png') is not None:
        ch2.append(pgui.locateOnScreen('rewards/ch2.png'))
        pyd.moveTo(ch2[0][0] + 100, ch2[0][1])
        pyd.click()
        pyd.click()


def confirmation():
    time.sleep(1)
    claim_button_coords = [1079, 780] #coordinates for the claim button x 1079, y 780
    ch_change_coords = [968, 600] #button to confirm ch change
    pyd.click(claim_button_coords[0], claim_button_coords[1])
    pyd.click(ch_change_coords[0], ch_change_coords[1])
    time.sleep(1)
    while pgui.locateOnScreen('rewards/lag_checker.png') is not None:
        time.sleep(4)



def claim_rewards():
    time.sleep(1)
    if lag_checker() >= lag_timer or lag_checker() == None:
        time.sleep(2)
        item_selector()
        time.sleep(2)
        ch_selector()
        confirmation()
        time.sleep(2)
    else:
        time.sleep(5)


def claim_rewards_no_check():
    time.sleep(2)
    item_selector()
    time.sleep(2)
    ch_selector()
    confirmation()
    time.sleep(2)


while True:
    #lag_checker()
    claim_rewards()
    #claim_rewards_no_check()
