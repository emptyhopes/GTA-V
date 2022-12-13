from pydirectinput import keyDown, keyUp, mouseDown, mouseUp
from time import sleep

from Modules.Logger import Print

def Run():
    mouseDown(button="left")
    sleep(20)
    mouseUp(button="left")