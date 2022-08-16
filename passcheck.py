import PySimpleGUI as sg
import os
import time

# Define the window's contents
layout = [
    [sg.Text("Enter the password."), sg.InputText(key='-TEXT-')],
    [sg.InputText(key = '-EPASS-')],
    [sg.Button("Ok"), sg.Button("Cancel")]
]

password = sg.Window('Şifre', layout)

while True:
    event, values = password.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        print("canceled")
        break

    if event == "Ok":
        if values['-EPASS-'] == "1234":
            print("ok")
            password.close()
            break
        else:
            print("wrong password")
            passwordtext = "Wrong Password!"
            password['-TEXT-'].update(passwordtext)
            time.sleep(2.5)
            passwordtext = "Enter the password."
            password['-TEXT-'].update(passwordtext)
            time.sleep(0.5)
        print("error 1")