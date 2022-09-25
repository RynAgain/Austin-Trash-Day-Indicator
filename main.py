import config #personal info keys
import rpiAPI #my own raspberry pi programing API
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.austintexas.gov/myschedule') #opens the starting webpage

def find_addbox(): #this will be a function for finding the 
    pass

def find_nextevent():
    pass
sleep(3)
addybox = driver.find_element(By.ID, 'row-input-0')
sleep(2)
addybox.send_keys(config.address)
sleep(2)
addybox.send_keys(Keys.ENTER)
sleep(1)
addybox.send_keys(Keys.ENTER)
sleep(100)
driver.close()
#This program will webscrape the Austin trash collection website and tell me what bins need to go out.
#vist https://www.austintexas.gov/myschedule
#webdrivers https://github.com/SergeyPirogov/webdriver_manager
#input address from config file    https://pythonspot.com/selenium-textbox/
#get next pickup date
#get the bins
#set to booleans
#make lights change
#if thursday run
#display on LCD info and who's turn it is to take the trash to curb.

#default webbrowswer? fire fox or chrome?

