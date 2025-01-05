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
from constants import *

pygame.init()
pygame.mixer.init()

# Init a window
window_width = 1000
window_height = 500
window = pygame.display.set_mode((window_width,window_height))

# Fonts
Times_new_roman_font = pygame.font.SysFont("Times New Roman", round(window_width/40))

class Button():
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = Times_new_roman_font

    def drawText(self, surface, text_color):
        """
        Draw only text on screen where the button located

        Param:
            surface (): The surface where it will be displayed.
            text_color (RGB color in set() defined): Color of text
        """
        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface,text_rect)

    def draw(self, surface, bg_color,  border_color, border_radius, border_width, text_color):
        """
        Draw both the Button and Text inside it
        Param:
            surface ():
            bg_color (): Background color
        """
        pygame.draw.rect(surface, bg_color, self.rect, 0, border_radius)

        if (border_width != 0):
            pygame.draw.rect(surface, border_color, self.rect, border_width, border_radius)
        
        self.drawText(surface, text_color)

# Setup buttons and stuffs
start_button = Button((window_width/2)*0.1, (window_height/3), (window_width/2)*0.8, (window_height/3)*0.8, "START")
stop_button = Button((window_width/2)*1.1, (window_height/3), (window_width/2)*0.8, (window_height/3)*0.8, "STOP")


# Init FPS
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    # Setup FPS for window
    clock.tick(FPS)

    # Process event 
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    # Background colors
    window.fill(WHITE)

    # Draw button 
   
    start_button.draw(window,GREEN, BLACK, 20, 5, text_color= WHITE)
    stop_button.draw(window,RED, BLACK, 20, 5, text_color= WHITE)

    # Update window frame by switching frame between Buffer and On-screen
    pygame.display.flip()


# Quit
pygame.mixer.stop()
pygame.quit()

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
def Pray(x):
    pgui.write("opray\n")
    time.sleep(5)
    x += 5
    return x

def Hunt(x):
    pgui.write("ohunt\n")
    time.sleep(5)
    x += 5
    return x


def Cash(x):
    pgui.write("ocash\n")
    time.sleep(7)
    x += 7
    return x

def Coinflip(x, ammount):
    """
    Play coinflip with an ammount of cash and sleep 8s.
    Param:
        x (int): timeVar
        ammount (int): ammount of cash to bet
    Return:
        x (int): timeVar after sleep 
    """
    pgui.write(f"ocoinflip {ammount}\n")
    time.sleep(8)
    x += 8
    return x

def RandomString(x):
    """
    Send a random String and sleep 10s.
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

def SLots(x, ammount):
    """
    Play slots with 100 cash
    """
    pgui.write("oslots 1000\n")
    time.sleep(8)
    x += 8
    return x

def DeepSleep(x):
    """
    Actual sleep for not invoke bot detect
    """
    time.sleep(45)
    x+=45
    return x

def Battle(x):
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

def startProcess():
    """
    Main function of program.
    """

    prevTimeVar = -20
    timeVar = 0

    # If not find Discord icon on screen then play notification and quit function

    # Else click into it

    
    # If timeVar is 0 then Pray

    # Else if already pass 20s then Hunt

    # Else if timeVar is larger than 300s (5min) then reset timeVar and prevTimeVar

    # Else perform random actions

    # If found VerifyTemplate then play notification and quit function