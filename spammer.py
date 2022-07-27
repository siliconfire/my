# imports
import os
import sys
import time
import pyautogui

# end of imports

version = 1.5
os.system('cls' if os.name == 'nt' else 'clear')
print("-----------------------------------------------------")
print("Welcome to text spammer.")
print("version: " + str(version))
print("")
print("made by github.com/trashbin7")
print("-----------------------------------------------------")
print("")
input("(!) Press ENTER to continue.")
os.system('cls' if os.name == 'nt' else 'clear')
print("-----------------------------------------------------")
print("Enter the text that you want to spam.")
print("")
print("")
print("made by github.com/trashbin7")
print("-----------------------------------------------------")
text = input("(!) Enter the text: ")

os.system('cls' if os.name == 'nt' else 'clear')
print("-----------------------------------------------------")
print("enter the delay between each text.")
print("")
print("")
print("made by github.com/trashbin7")
print("-----------------------------------------------------")
delay = input("(!) Enter the delay: ")

os.system('cls' if os.name == 'nt' else 'clear')
print("-----------------------------------------------------")
print("enter the number of times you want to spam the text.")
print("")
print("")
print("made by github.com/trashbin7")
print("-----------------------------------------------------")
times = input("(!) Enter the number of times: ")

print("-----------------------------------------------------")
print("Spamming is going to be turned on in 10 seconds.")
print("")
print("")
print("made by github.com/trashbin7")
print("-----------------------------------------------------")
time.sleep(10)

while times != 0:
    pyautogui.write(text, interval=0.1)             # write the text and sets an interval to prevent bad use of this program                     # wait for the delay
    times = int(times) - 1
    print("-----------------------------------------------------")
    print(str(times) + "times left.")
    print("")
    print("")
    print("made by github.com/trashbin7")
    print("-----------------------------------------------------")
    time.sleep(int(delay))                               # wait for the delay
    os.system('cls' if os.name == 'nt' else 'clear')                                # clear the screen

# end of code