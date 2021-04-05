'''
Copyright © 2021 Michael Fang
A python script that play the dino game on Chrome automatically.
I AM ONLY 13!!
GitHub: FangziOMG
Follow me on twitter: @MichaelFangzi
'''

from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *

restartbtn = (955, 490) # Location of the restart button
dino = (625, 520) #location of the dinosaur

def replay(): #replay
    pyautogui.click(restartbtn)
    print('Restarted Game')

def detect(): #detect whether their is a obstacle
    drange = (dino[0]+28, dino[1], dino[0]+136.5, dino[1]+5)
    img = ImageGrab.grab(drange)
    obs = ImageOps.grayscale(img)
    arr = array(obs.getcolors())
    return arr.sum()


time.sleep(4) #Go to www.trex-game.skipser.com during this time
replay()

while True: #detect every single moment
    detect()
    if (detect() != 792): #check whether their is a obstacle
        pyautogui.keyDown('space') #press spacebar (jump)
