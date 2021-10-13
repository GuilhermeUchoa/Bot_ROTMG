import PySimpleGUI as sg

sg.theme('Dark Blue 3')   # Add a touch of color
# All the stuff inside your window.
layout = [ [sg.Button('Bot_on'),sg.Button('Auto_Nexus'),sg.Button('Auto_loot'),sg.Button('Auto_HP')]]

# Create the Window
window = sg.Window('Bot_Realm of the Mad God Exalt', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED : 
        break

    if event == 'Bot_on' :
        from main import *
        

