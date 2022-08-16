import PySimpleGUI as sg
import os
import time


layout = [
    [sg.Text("The best menu ever! (made by github.com/trashbin7)", key = "-TEXT-"),],
    [sg.Button("Bye!")]
]


password = sg.Window('Password', layout)

while True:
    event, values = password.read()

    if event == sg.WIN_CLOSED or event == 'Bye!':
        print("Bye!!!!!!!!")
        break