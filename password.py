print("loading...")
import time        # Import the time module to use the sleep function
import random      # Import the random module to use the randint function
import sys         # Import the sys module to use the exit function
import os          # Import the os module to use the system function
import keyboard    # Import the keyboard module to use the is_pressed function
from colorama import Fore, Back, Style
pickedlength = False
pickedtype = False
showingpassword = False
timehere = 0
password = ""
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
keyboard.press_and_release("backspace")
os.system('cls' if os.name == 'nt' else 'clear')
print("-----------------------------------------------------")
print("Pick a type of password:")
print("")
print("[A] Only letters")
print("[B] Letters and numbers")
print("[C] Letters, numbers and symbols")
print("")
print("-----------------------------------------------------")
while pickedtype == False:
    if keyboard.is_pressed("a"):
        type = "l"
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------------------------")
        print("Pick a type of password:")
        print("")
        print(Fore.GREEN + "[A] Only letters")
        print(Style.RESET_ALL + "[B] Letters and numbers")
        print("[C] Letters, numbers and symbols")
        print("")
        print("-----------------------------------------------------")
        time.sleep(0.3)
        pickedtype = True
    elif keyboard.is_pressed("b"):
        type = "ln"
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------------------------")
        print("Pick a type of password:")
        print("")
        print("[A] Only letters")
        print(Fore.GREEN + "[B] Letters and numbers")
        print(Style.RESET_ALL + "[C] Letters, numbers and symbols")
        print("")
        print("-----------------------------------------------------")
        time.sleep(0.3)
        pickedtype = True
    elif keyboard.is_pressed("c"):
        type = "lns"
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------------------------------")
        print("Pick a type of password:")
        print("")
        print("[A] Only letters")
        print("[B] Letters and numbers")
        print(Fore.GREEN + "[C] Letters, numbers and symbols")
        print(Style.RESET_ALL)
        print("-----------------------------------------------------")
        time.sleep(0.3)
        pickedtype = True
keyboard.press_and_release("backspace")
if type == "l":
    for i in range(length):
        password = password + random.choice("abcdefghijklmnopqrstuvwxyz")
elif type == "ln":
    for i in range(length):
        password = password + random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
elif type == "lns":
    for i in range(length):
        password = password + random.choice("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()")
os.system('cls' if os.name == 'nt' else 'clear')
print("-----------------------------------------------------")
print("Your very random password is:")
print("XXXXXXXX")
print("")
print("[A] Show password")
print("")
print("")
print("-----------------------------------------------------")
keyboard.wait("a")
os.system('cls' if os.name == 'nt' else 'clear')
keyboard.press_and_release("backspace")
print("-----------------------------------------------------")
print("Your very random password is:")
print(password)
print("")
print(Fore.GREEN + "[A] Show password")
print(Style.RESET_ALL + "[B] Write password")
print("[C] Exit")
print("-----------------------------------------------------")
print("")
print("(!) wait before typing A, B or C")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    timehere = timehere + 1 
    print("-----------------------------------------------------")
    print("Your very random password is:")
    print(password)
    print("(" + str(timehere) + " seconds)")
    print("")
    print("[B] Write password")
    print("[C] Exit")
    print("-----------------------------------------------------")
    if keyboard.is_pressed("b"):
        keyboard.press_and_release("backspace")
        print("Typing the password in 5 seconds...")
        time.sleep(5)
        keyboard.write(password)
        print("task complete!")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    elif keyboard.is_pressed("c"):
        keyboard.press_and_release("backspace")
        print("Bye!")
        time.sleep(1.5)
        sys.exit()