import pyautogui as pgui
from QueueArray import QueueArray 
from random import Random
import time

pgui.moveTo(1250,1049)
pgui.click()

prevTimeVar = -20
timeVar = 0

actionsQueue = QueueArray(size=3)
def A(timeVar):
    pgui.write("opray\n")
    time.sleep(3)
    timeVar += 3
    return timeVar

def B(timeVar):
    pgui.write("ohunt\n")
    time.sleep(3)
    timeVar += 3
    return timeVar


def C(timeVar):
    pgui.write("ozoo\n")
    time.sleep(5)
    timeVar += 5
    return timeVar

def D(timeVar):
    pgui.write("ohb\n")
    time.sleep(5)
    timeVar += 5
    return timeVar

def E(timeVar):
    time.sleep(10)
    timeVar += 10
    return timeVar

def F(timeVar):
    pgui.write("ohelp\n")
    time.sleep(5)
    timeVar += 5
    return timeVar

def PerformQueue(timeVar):
    rand = Random()
    actions = [C, D, E, F]

    while (actionsQueue.isFull() is False):
        action = actions[rand.randint(0,3)]

        if (actionsQueue.isContains(action) is False):
            actionsQueue.enQueue(action)

    while (actionsQueue.isEmpty() is False):
        act = actionsQueue.deQueue()
        timeVar += act(timeVar)

    return timeVar
    

for i in range(10):

    if (timeVar == 0):
        timeVar += A(timeVar)
    elif (timeVar - prevTimeVar >= 20):
        timeVar += B(timeVar)
        prevTimeVar = timeVar
    elif (timeVar >= 300):
        prevTimeVar = 0 - timeVar + 300
        timeVar = 0
    else:
        timeVar += PerformQueue(timeVar)