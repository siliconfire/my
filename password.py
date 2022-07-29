print("loading...")
import time        # Import the time module to use the sleep function
import random      # Import the random module to use the randint function
import sys         # Import the sys module to use the exit function
import os          # Import the os module to use the system function
import keyboard    # Import the keyboard module to use the is_pressed function
from colorama import Fore, Back, Style
pickedlength = False
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print("-----------------------------------------------------")
print("Welcome to the password generator!")
print("This program will generate a random password for you.")
print("")
print(Fore.GREEN + "(!) press [Enter] to start.")
print(Style.RESET_ALL)
print("github.com/trashbin7")
print("-----------------------------------------------------")

keyboard.wait("enter")
time.sleep(0.3)
os.system('cls' if os.name == 'nt' else 'clear')

print("-----------------------------------------------------")
print("Welcome to the password generator!")
print("This program will generate a random password for you.")
print("")
print("")
print("")
print("github.com/trashbin7")
print("-----------------------------------------------------")
time.sleep(0.3)
os.system('cls' if os.name == 'nt' else 'clear')
print("-----------------------------------------------------")
print("Welcome to the password generator!")
print("This program will generate a random password for you.")
print("")
print(Fore.GREEN + "(!) press [Enter] to start.")
print(Style.RESET_ALL)
print("github.com/trashbin7")
print("-----------------------------------------------------")
time.sleep(0.3)
os.system('cls' if os.name == 'nt' else 'clear')


print("-----------------------------------------------------")
print("Pick a password length:")
print("")
print("[A] 8 characters")
print("[B] 12 characters")
print("[C] 16 characters")
print("")
print("-----------------------------------------------------")
while pickedlength == False:
    if keyboard.is_pressed("a"):
        length = 8
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------------------------")
        print("Pick a password length:")
        print("")
        print(Fore.GREEN + "[A] 8 characters")
        print(Style.RESET_ALL + "[B] 12 characters")
        print("[C] 16 characters")
        print("")
        print("-----------------------------------------------------")
        time.sleep(0.3)
        pickedlength = True
    elif keyboard.is_pressed("b"):
        length = 12
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------------------------")
        print("Pick a password length:")
        print("")
        print("[A] 8 characters")
        print(Fore.GREEN + "[B] 12 characters")
        print(Style.RESET_ALL + "[C] 16 characters")
        print("")
        print("-----------------------------------------------------")
        time.sleep(0.3)
        pickedlength = True
    elif keyboard.is_pressed("c"):
        length = 16
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------------------------")
        print("Pick a password length:")
        print("")
        print("[A] 8 characters")
        print("[B] 12 characters")
        print(Fore.GREEN + "[C] 16 characters")
        print(Style.RESET_ALL)
        print("-----------------------------------------------------")
        time.sleep(0.3)
        pickedlength = True

print("-----------------------------------------------------")
print("Pick a type of password:")
print("")
print("")
print("")
print("")
print("")
print("-----------------------------------------------------")