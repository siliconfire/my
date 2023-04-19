import pyautogui
import time

counter = 0
Triedagain = False
Triedagain2 = False

print("github.com/trashbin7")
while Triedagain2 == False:
    if Triedagain == False:
        enteredpass = pyautogui.password(text='Enter the password', title='owo hunt', default='', mask='*')
    elif Triedagain == True:
        enteredpass = pyautogui.password(text='Your password was wrong. Try again!', title='owo hunt', default='', mask='*')

    if enteredpass == "owobot14":
        print("Password correct")
        print("")
        stopat = input("stop at: ")
        time.sleep(1)
        print("Remaining time: 15 saniye")
        time.sleep(1)
        print("Remaining time: 14 saniye")
        time.sleep(1)
        print("Remaining time: 13 saniye")
        time.sleep(1)
        print("Remaining time: 12 saniye")
        time.sleep(1)
        print("Remaining time: 11 saniye")
        time.sleep(1)
        print("Remaining time: 10 saniye")
        time.sleep(1)
        print("Remaining time: 9 saniye")
        time.sleep(1)
        print("Remaining time: 8 saniye")
        time.sleep(1)
        print("Remaining time: 7 saniye")
        time.sleep(1)
        print("Remaining time: 6 saniye")
        time.sleep(1)
        print("Remaining time: 5 saniye")
        time.sleep(1)
        print("Remaining time: 4 saniye")
        time.sleep(1)
        print("Remaining time: 3 saniye")
        time.sleep(1)
        print("Remaining time: 2 saniye")
        time.sleep(1)
        print("Remaining time: 1 saniye")
        time.sleep(1)
        print("(!) Starting... Now!")
        print("(i) Press ctrl + c to stop this bot.")
        while True:
            pyautogui.write('owo hunt', interval=0.2)
            time.sleep(1)
            pyautogui.press("Enter")
            counter = counter + 1
            print("typed owo hunt " + str(counter) + " times")
            time.sleep(20)
            if counter == int(stopat):
                while True:
                    print("finished")
                    time.sleep(2)
    else:
        if Triedagain == False:
            print("(!) Wrong password! Try again.")
            print()
            Triedagain = True
        elif Triedagain == True:
            print()
            print("Wrong password again???")
            input("(!) Press [ENTER] to exit.")
            Triedagain2 = True
