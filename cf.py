from selenium import webdriver
from selenium.webdriver.edge.options import Options
import pyautogui as pygui

import os

class cf(webdriver.Edge):
    def __init__(self, driver_path = r'F:\PythonProject\Python_Selenium\WebDriver'):
        self.driver_path = driver_path
        self.options = Options()

        self.options.add_argument('--inprivate')
        

        os.environ['PATH'] += self.driver_path
        super(cf,self).__init__(options=self.options)

    def __exit__(self, exc_type, exc, traceback):
        self.quit()
            
    
        
    def accessToPage(self, inUrl):
        """
        Access to a certain Page without open in new Tab

        Param: 
            inUrl: String
        """
        self.get(inUrl)

    def clickToPosition(self, locX, locY):
        """
        Move mouse to a specific location on Screen and click.
        """
        pygui.click(locX,locY)

    
    

   

    
    

        