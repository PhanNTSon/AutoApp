import pyautogui as pgui
import time

pgui.moveTo(1250,1049)
pgui.click()
timeVar = 0
sleepTime = 20
pray = "opray\n"
hunt = "ohunt\n"
firstTime = True

for i in range(100):    
    if (firstTime):
        pgui.write(pray)
        time.sleep(5)
        pgui.write(hunt)
        firstTime = False
        timeVar = 0
    elif (timeVar /300 > 1):
        pgui.write(pray)
        time.sleep(5)
        pgui.write(hunt)
        timeVar = 0
    # Else ohunt only
    else:
        pgui.write(hunt)


    time.sleep(sleepTime)
    timeVar+=sleepTime

