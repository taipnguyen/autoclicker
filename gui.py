import mouse
import time
from sense_and_click import click_with

# hello_psg.py

import PySimpleGUI as sg

layout = [[sg.Text("1.) Enter values \n2.) Press autoclick\n3.) Set mouse at location where you want to click")],
[sg.Text("Clicks"),sg.In(size=(5, 1), enable_events=True, key="-CLICKS-")
,sg.Text("Speed (0-1)"),sg.In(size=(5, 1), enable_events=True, key="-SPEED-")],
 [sg.Button("Autoclick")],[sg.Button("Close")]
 ]

# Create the window
window = sg.Window("Autoclicker", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    if event == "Autoclick":
        clicks = int(values["-CLICKS-"])
        time_btwn = 1 - float(values["-SPEED-"])
        time.sleep(2)
        time_btwn = 0.5
        click_with(clicks,time_btwn)


window.close()
