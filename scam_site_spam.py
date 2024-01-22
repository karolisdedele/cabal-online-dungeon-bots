import string
import time

import requests
import random
import threading

def main_func():
    id = string.ascii_uppercase + string.digits
    post_id = ''.join(random.sample(id, 10))
    post_pw = ''.join(random.sample(id, 10))
    post_pin = random.randint(1234, 999999)
    link = "https://submit-form.com/moRRvWxd"
    r = requests.post(link, data={'ID': post_id, 'Password': post_pw, "pin": post_pin})
    print(post_id, post_pw, post_pin)
    print(r.status_code, r.reason, r.url)

threads = []

def run():

    for _ in range(2):
        t = threading.Thread(target=main_func)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

while True:
    run()
    time.sleep(0.5)