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
    Play coinflip with 100 cash
    """
    pgui.write("ocoinflip 100\n")
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
        "朝\n",
        "夜\n",
        "昼\n",
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
    pgui.write("oslots 100\n")
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

def PerformQueue(x):
    rand = Random()
    actions = [C, D, E, F]

    while (actionsQueue.isFull() is False):

        ind = rand.randint(0,3)
        action = actions[ind]

        if ind is 2:
            actionsQueue.enQueue(action)

        if (actionsQueue.isContains(action) is False):
            actionsQueue.enQueue(action)

    while (actionsQueue.isEmpty() is False):
        act = actionsQueue.deQueue()
        x = act(x)

    return x

loopNum = 0    

while True:

    loopNum +=1

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

    if (loopNum == 100):
        timeVar = G(timeVar)
