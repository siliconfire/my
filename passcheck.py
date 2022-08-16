import PySimpleGUI as sg
import os
import time
wrongpass = 0
passwordcorrect = False
layout = [
    [sg.Text("Enter the password.", key = "-TEXT-"),],
    [sg.InputText(key = '-EPASS-')],
    [sg.Button("Ok"), sg.Button("Cancel")]
]

password = sg.Window('Password', layout)

while True:
    event, values = password.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        print("canceled")
        break

    if event == "Ok":
        password['-TEXT-'].update(f"Checking...")
        password.refresh()


        if values['-EPASS-'] == "1234":
            passwordcorrect = True
            time.sleep(2)
            break


        else:
            wrongpass = wrongpass + 1
            password['-TEXT-'].update(f"Wrong password. Try again. ({wrongpass} wrong attempts)")
            time.sleep(1)


if passwordcorrect == True:
    password['-TEXT-'].update(f"Loading...")
    password.refresh()
    print("password correct, going to main.py")
    time.sleep(1)
    password.close()
    os.system("python3 main.py")

else:
    print("password incorrect, exiting")