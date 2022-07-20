import pyautogui
import time
counter = 0

print("-------------------------------------")
print("owoh yazan bot v1.1")
print("")
print("bu bot otomatik olarak 20 saniyede bir owoh yazacaktır.")
print("github.com/trashbin7")
print("-------------------------------------")
print("")
print("")
print("")
print("(!) bot 15 saniye içinde başlayacaktır, discorda geçin.")
time.sleep(15)
print("bot aktif...")
while True:
    pyautogui.write('owo hunt', interval=0.1)
    time.sleep(1)
    pyautogui.press("Enter")
    counter = counter + 1
    print("bot " + str(counter) + " kez yazdı")
    time.sleep(20)