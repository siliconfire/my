# WARNING:
# i am not responsible for any damage caused by this program.
#
# Not running? 
# Try installing pyautogui (type "pip install pyautogui" on the terminal.)



#imports are here - dont touch
print("loading...")
import os
import time

import pyautogui
from colorama import Back, Fore, Style

ver = 1.1

#imports are here - dont touch


os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n[Setup]->[Confirmation]->[Run]" + Fore.BLUE + "\n\n(!) Press [ENTER] to start."+ Style.RESET_ALL + f"\n(i) always remember that you can quit with Ctrl+C at any time.\n\nmade by github.com/TrashBin7 (V{ver})\n--------------------------------------------------")
input()

os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n" + Fore.GREEN + "[Setup]" + Style.RESET_ALL + "->[Confirmation]->[Run]\n\n(!) Please enter the text that you want to spam\nand press [ENTER].\n\nmade by github.com/Trashbin7\n--------------------------------------------------")
text = input()
os.system('cls' if os.name == 'nt' else 'clear')
print("-----------------------------------------------\n" + Fore.GREEN + "[Setup]->" + Style.RESET_ALL + "[Confirmation]->[Run]\n\n(!) Type how many times you want to spam\nand press [ENTER].\n\nmade by github.com/Trashbin7\n--------------------------------------------------")
times = input()
os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n" + Fore.GREEN + "[Setup]->[Confirmation]" + Style.RESET_ALL + f"->[Run]\n\nText: {text}, Times: {times}.\n" + Fore.BLUE + "(!) Press [ENTER] to continue." + Style.RESET_ALL + "\n\nmade by github.com/Trashbin7\n--------------------------------------------------")
input()
os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n" + Fore.GREEN + "[Setup]->[Confirmation]->" + Style.RESET_ALL + "[Run]\n\n" + Fore.RED + "WARNING: I am NOT responsible for any damage caused by this program.\n" + Fore.BLUE + "(!) Press [ENTER] to start spamming." + Style.RESET_ALL + "\n\nmade by github.com/Trashbin7\n--------------------------------------------------")
input()
confirm = pyautogui.confirm(text='Do you really want to start spamming?', title='Question', buttons=['OK', 'Cancel'])
if confirm == "OK":
    print("You Picked 'Continue'.")
    time.sleep(0.5)
else:
    while True:
        print("you picked Cancel or closed the window.")
        print("press ctrl+c to exit")
        print()
        time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n" + Fore.GREEN + "[Setup]->[Confirmation]->[Run (in 5 seconds...)]" + Style.RESET_ALL + "\n\nRunning in 5 seconds.\n--------------------\n\nmade by github.com/TrashBin7\n--------------------------------------------------")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n" + Fore.GREEN + "[Setup]->[Confirmation]->[Run (in <5 seconds...)]" + Style.RESET_ALL + "\n\nRunning in 4 seconds.\n####----------------\n\nmade by github.com/TrashBin7\n--------------------------------------------------")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n" + Fore.GREEN + "[Setup]->[Confirmation]->[Run (in <5 seconds...)]" + Style.RESET_ALL + "\n\nRunning in 3 seconds.\n########------------\n\nmade by github.com/TrashBin7\n--------------------------------------------------")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n" + Fore.GREEN + "[Setup]->[Confirmation]->[Run (in <5 seconds...)]" + Style.RESET_ALL + "\n\nRunning in 2 seconds.\n############--------\n\nmade by github.com/TrashBin7\n--------------------------------------------------")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n" + Fore.GREEN + "[Setup]->[Confirmation]->[Run (in <5 seconds...)]" + Style.RESET_ALL + "\n\nRunning in 1 seconds.\n################----\n\nmade by github.com/TrashBin7\n--------------------------------------------------")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------------------\n" + Fore.GREEN + "[Setup]->[Confirmation]->[Running...]" + Style.RESET_ALL + "\n\nJust a moment...\n###################\n\nmade by github.com/TrashBin7\n--------------------------------------------------")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
times = int(times)
while times != 0: 
    pyautogui.write(str(text))
    print(f"Spamming, {times} left.")
    times = times - 1