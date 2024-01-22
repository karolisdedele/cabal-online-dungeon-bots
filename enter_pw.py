import pyautogui as pgui
from cryptography.fernet import Fernet

pgui.PAUSE=0.001

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

pw_encoded = open("pw.txt", 'rb')
key = input("paste encode key: ")
pw_encoded = pw_encoded.read()
Decrypted=decrypt(pw_encoded, key).decode()
print(Decrypted)
while True:
    if pgui.locateOnScreen('enter_password.png', confidence=0.9) is not None:
        pgui.typewrite(Decrypted)
        print("typing ")
        break