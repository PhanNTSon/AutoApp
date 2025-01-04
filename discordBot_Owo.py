import cv2
import numpy as np
import pyautogui as pgui
import pygame
import time

"""
OpenCV: cv2
    Using this library for template matching, finding whether the template is existed or not.
numpy
    Convert a picture into an array (smth like that) so the cv2 can read and locate the actual location on screen.
pyautogui
    Control mouse, keyboard and other stuffs.
"""

from QueueArray import QueueArray 
from random import Random

pygame.mixer.init()

discordIconTemplate = r"F:\PythonProject\AutoApp\images\discordIcon_template.png"

winCoinFlipTemplate = r"F:\PythonProject\AutoApp\images\winCoinFlip_template.png"
lostCoinFlipTemplate = r"F:\PythonProject\AutoApp\images\lostCoinFlip_template.png"
verifyTemplate = r"F:\PythonProject\AutoApp\images\verify_template.png"


# pgui.moveTo(1250,1049)
# pgui.click()

def playNotification():
    """
    Playing notification sound til' it end.
    Sound: Homecoming - Samsung Ringtone.mp3.

    """
    pygame.mixer.music.load("F:\PythonProject\AutoApp\sounds\Homecoming - Samsung Ringtone.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass

def isTemplateExisted(templateSrc):
    """
    Check if template is exist on screen by using openCV(cv2).

    Param:
        templateSrc: Path of template
    
    Return:
        An array:   [0] True/ False
                    [1] Location x: Int/ None
                    [2] Location y: Int/ None
    """
    
    # Capture screenshot
    screenshot = pgui.screenshot()

    # Convert into numpy
    screen = np.array(screenshot)
    # Convert from RGB to BRG (cv2 using BRG)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    
    # Read template
    template = cv2.imread(templateSrc, cv2.IMREAD_COLOR)
    # Get matrix result after matching with template
    result = cv2.matchTemplate(screen,template,cv2.TM_CCOEFF_NORMED)

    # Get min,max value and location of matrix
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # If maxVal is larger than 0.8 then return value
    if max_val >= 0.9:
        return [True,
                max_loc[0],
                max_loc[1]
                ]
    
    # Else return False
    else:
        return [False,
                None,
                None
                ]

    


actionsQueue = QueueArray(size=3)
def A(x):
    pgui.write("opray\n")
    time.sleep(5)
    x += 5
    return x

def B(x):
    pgui.write("ohunt\n")
    time.sleep(5)
    x += 5
    return x


def C(x):
    pgui.write("ocash\n")
    time.sleep(7)
    x += 7
    return x

def D(x):
    """
    Play coinflip with 1000 cash
    """
    pgui.write("ocoinflip 1000\n")
    time.sleep(8)
    x += 8
    return x

def E(x):
    """
    Send a random String
    """

    collectString = [
        "sleep :))\n",
        "bruh\n",
        "3tocom\n",
        "mamamia\n",
        "cyka blyat\n",
        "anhbasin\n"
    ]

    seed = Random()

    pgui.write(f"{collectString[seed.randint(0,5)]}\n")
    time.sleep(10)
    x += 10
    return x

def F(x):
    """
    Play slots with 100 cash
    """
    pgui.write("oslots 1000\n")
    time.sleep(8)
    x += 8
    return x

def G(x):
    """
    Actual sleep for not invoke bot detect
    """
    time.sleep(45)
    x+=45
    return x

def H(x):
    """
    Battle
    """
    pgui.write("obattle\n")
    time.sleep(10)
    x += 10
    return x

def PerformQueue(x):
    rand = Random()
    actions = [C, D, E, F, H]

    while (actionsQueue.isFull() is False):

        ind = rand.randint(0,4)
        action = actions[ind]

        if ind == 2:
            actionsQueue.enQueue(action)

        if (actionsQueue.isContains(action) is False):
            actionsQueue.enQueue(action)

    while (actionsQueue.isEmpty() is False):
        act = actionsQueue.deQueue()
        x = act(x)

    return x



r1 = isTemplateExisted(discordIconTemplate)
print(r1)
if (r1[0] is True):
    pgui.click(r1[1],r1[2])

    time.sleep(2)

    r = isTemplateExisted(verifyTemplate)

    print(r)
else:
    playNotification()