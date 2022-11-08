import time
import digitalio
import board
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

"""MY BUTTONS"""

copy = board.GP16
paste = board.GP17
save = board.GP15
undo = board.GP1
prnt = board.GP0
"""List of buttons to save code later"""
btns = [copy,paste,save,undo,prnt]

"""KEYBOARD SHORTCUTS"""

keyboard = Keyboard(usb_hid.devices)

"""combination is executed"""
def copyF():
    keyboard.press(Keycode.C,Keycode.CONTROL)
    time.sleep(0.1)
    keyboard.release(Keycode.C,Keycode.CONTROL)
    
def pasteF():
    keyboard.press(Keycode.V,Keycode.CONTROL)
    time.sleep(0.1)
    keyboard.release(Keycode.V,Keycode.CONTROL)
    
def saveF():
    keyboard.press(Keycode.S,Keycode.CONTROL)
    time.sleep(0.1)
    keyboard.release(Keycode.S,Keycode.CONTROL)
    
def undoF():
    keyboard.press(Keycode.Z,Keycode.CONTROL)
    time.sleep(0.1)
    keyboard.release(Keycode.Z,Keycode.CONTROL)

def printF():
    keyboard.press(Keycode.P,Keycode.CONTROL)
    time.sleep(0.1)
    keyboard.release(Keycode.P,Keycode.CONTROL)
    

"""List of commands ready to be called"""
"""IMPORTANT! Buttons list and commands lsit MUST match in order"""
coms = [copyF,pasteF,saveF,undoF,printF]

"""Buttons initialization"""
for i in range (len(btns)):
    btns[i] = digitalio.DigitalInOut(btns[i])
    btns[i].direction = digitalio.Direction.INPUT
    btns[i].pull = digitalio.Pull.UP


"""'Listening' for button press and executing command"""
while True:
    for i in range (len(btns)):
        if not btns[i].value:
            coms[i]()
    time.sleep(0.2)        