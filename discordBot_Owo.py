import pyautogui as pgui
import time

pgui.moveTo(1250,1049)
pgui.click()
timeVar = 0

for i in range(100):    
    if (timeVar != 0 and timeVar != 300):
        timeVar = 0
        pgui.write('ohunt\n')
    else:
        pgui.write('opray\n')
    time.sleep(20)
    timeVar+=20


