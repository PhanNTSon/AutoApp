import pyautogui as pgui
import time

pgui.moveTo(1205,1049)
pgui.click()
for i in range(100):    
    pgui.write('ohunt\n')
    time.sleep(20)

