# imports
import os
import sys
import time
import pyautogui

# end of imports

version = 0.4

os.system("cls")
print("-----------------------------------------------------")
print("Welcome to text spammer.")
print("version: " + str(version))
print("")
print("made by github.com/trashbin7")
print("-----------------------------------------------------")
print("")
input("(!) Press ENTER to continue.")
os.system("cls")
print("-----------------------------------------------------")
print("Enter the text that you want to spam.")
print("")
print("")
print("made by github.com/trashbin7")
print("-----------------------------------------------------")
text = input("(!) Enter the text: ")

os.system("cls")
print("-----------------------------------------------------")
print("enter the delay between each text.")
print("")
print("")
print("made by github.com/trashbin7")
print("-----------------------------------------------------")
delay = input("(!) Enter the delay: ")

os.system("cls")
print("-----------------------------------------------------")
print("enter the number of times you want to spam the text.")
print("(put 0 to spam until you close this screen)")
print("")
print("made by github.com/trashbin7")
print("-----------------------------------------------------")
times = input("(!) Enter the number of times: ")

while times != 0:
    pyautogui.write(text, interval=0.1)             # write the text and sets an interval to prevent bad use of this program                     # wait for the delay
    times = times - 1                               # decrease the times
    print("(!) " + str(times) + " times left.")     # print the times left
    time.sleep(delay)                               # wait for the delay
    os.system("cls")                                # clear the screen

# end of code