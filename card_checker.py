import requests
import json
import random
import time
import pydirectinput as pyd
import pyautogui as pgui
import pyscreeze as pscr

if pscr.locateOnScreen("nectar.png") is not None:
    print("hey")

"""with open("card_numbers.txt", 'w') as my_file:
    my_file.write("existing cards \n")
    # for i in range(10,99):
    card_num = "168105{}017".format(20)
    # print(card_num)
    payload = {
        "cardNumber": card_num
    }
    time.sleep(3)
    r = requests.post(url, payload)
    print(r.reason)
    http_response = r.json()
    # print(http_response['response'])
    if http_response['response'] is not None:
        my_file.write(f"{card_num} \n")
        print(f"{card_num} written in file")
    else:
        pass"""
