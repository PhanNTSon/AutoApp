import pyautogui as pgui
from QueueArray import QueueArray 
from random import Random
import time

pgui.moveTo(1250,1049)
pgui.click()

prevTimeVar = -20
timeVar = 0

actionsQueue = QueueArray(size=3)
def A(x):
    pgui.write("opray\n")
    time.sleep(3)
    x += 3
    return x

def B(x):
    pgui.write(f"ohunt{x+3}\n")
    time.sleep(3)
    x += 3
    return x


def C(x):
    pgui.write(f"ocash{x+7}\n")
    time.sleep(7)
    x += 7
    return x

def D(x):
    pgui.write(f"ohb{x+7}\n")
    time.sleep(7)
    x += 7
    return x

def E(x):
    pgui.write(f"sleep :)){x+10}\n")
    time.sleep(10)
    x += 10
    return x

def F(x):
    pgui.write(f"ohelp{x+7}\n")
    time.sleep(7)
    x += 7
    return x

def PerformQueue(x):
    rand = Random()
    actions = [C, D, E, F]

    while (actionsQueue.isFull() is False):
        action = actions[rand.randint(0,3)]

        if (actionsQueue.isContains(action) is False):
            actionsQueue.enQueue(action)

    while (actionsQueue.isEmpty() is False):
        act = actionsQueue.deQueue()
        x = act(x)

    return x
    

for i in range(10):

    if (timeVar == 0):
        timeVar = A(timeVar)
    elif (timeVar - prevTimeVar >= 20):
        timeVar = B(timeVar)

        prevTimeVar = timeVar
    elif (timeVar >= 300):
        prevTimeVar = 0 - timeVar + 300
        timeVar = 0
    else:
        timeVar = PerformQueue(timeVar)

    print(timeVar)