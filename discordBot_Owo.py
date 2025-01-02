import pyautogui as pgui
from QueueArray import QueueArray 
from random import Random
import time

pgui.moveTo(1250,1049)
pgui.click()

prevTimeVar = 0
timeVar = 0

actions = [
    "opray\n",
    "ohunt\n",
    "ozoo\n",
    "ohb\n"
]

actionsQueue = QueueArray()

def genSmthElse():
    rand = Random()
    x = rand.randint(2,4)
    if (x != 4):
        return actions[x]
    else:
        return "sleep"

def doSmthElse(action):
    if (action != "sleep"):
        pgui.write(action)
        time.sleep(5)
    else:
        time.sleep(5)
    return 5
    

def isAvailableHunt(present, previous):
    if ((present - previous) >= 20):
        return True
    else:
        return False
    
# Loop for 100 times
for i in range (20):

    # If time is 0 then pray, sleep 5s and hunt
    if (timeVar == 0):
        pgui.write(actions[0])
        time.sleep(5)
        pgui.write(actions[1])

        prevTimeVar = timeVar
        timeVar += 5
    # Else if available to hunt then hunt
    elif (isAvailableHunt(timeVar,prevTimeVar)):
        pgui.write(actions[1])
        prevTimeVar = timeVar

    # Else not available to hunt then do smth else
    else:
        passTime = doSmthElse(genSmthElse())
        prevTimeVar = timeVar
        timeVar += passTime

    # If time is more than 300s then reset back to 0
    if (timeVar >= 300):
        prevTimeVar =  0 - (timeVar - prevTimeVar)
        timeVar = 0
