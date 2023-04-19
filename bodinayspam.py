import pyautogui
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')
counter = 0
input("BODINAY spamlamak için [ENTER] bas.")
countermax = int(input("MAX: "))
print("Çıkmak için ctrl+c bas.")
time.sleep(5)
print()
while counter <= countermax:
    pyautogui.write("BODDİNAY BODDİNAY BAODDİNAY DÜM DÜM DÜM DÜMDÜMBODDİNAY BODDİNAY BAODDİNAY DÜM DÜM DÜM DÜMDÜM")
    time.sleep(1)
    pyautogui.press("ENTER")
    counter = counter + 1
    print(counter)
    time.sleep(2)
