import pyautogui
import time
import keyboard
import tkinter as tk
from tkinter import simpledialog
import PySimpleGUI as sg

def checkIfHighlight():
  if(pyautogui.pixelMatchesColor(326, 371, (231, 180, 119))):
      return True
  return False

def searchQueryOut(query):
   pyautogui.moveTo(480, 899)
   pyautogui.leftClick() 
   pyautogui.write(query)


def altSpam():
    pyautogui.moveTo(112, 264)
    pyautogui.rightClick()
    pyautogui.keyDown('shift')
    pyautogui.moveTo(343,460)
    while(True):
       if keyboard.is_pressed('space'):
          pyautogui.keyUp('shift')
          break
       if checkIfHighlight():
          pyautogui.keyUp('shift')
          break
       pyautogui.leftClick()

def altRoll(query):
   searchQueryOut(query)
   altSpam()

time.sleep(2)
#searchQueryOut("poggers people");
#checkIfHighlight()

#pyautogui.moveTo(438, 275)
#pyautogui.leftClick()  
#print(pyautogui.position())
#altSpam()
#checks to see if it actually matches
# Top level window


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Press Space to Break Out of Rolling')],
            [sg.Text('Enter Mod Rolling For: '), sg.InputText()],
            [sg.Button('Alt Spam'), sg.Button('Alt Regal (Coming Soon)'),] ]

# Create the Window
window = sg.Window('Pog Layout', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Alt Regal': # if user closes window or clicks cancel
        break
    elif event == 'Alt Spam':
       altRoll(values[0])

window.close()
#altRoll(USER_INP)




#locations of things:
#highlighted item: (326,371)
#item to click on: (343,460)
#searchbox: (480,899)
#alts: (112,264)
#regals: (438, 275)
#transmutes: (56,265)
#scours: (433,512)
