#IMPORTS AND OTHER FILES
import config #personal info keys
import rpiAPI #my own raspberry pi programing API
from time import sleep #import the sleep function
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#VARIABLES

#drivers below need to be moved to the main code section
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.austintexas.gov/myschedule') #opens the starting webpage

def find_addybox(): #this will be a function for finding the address box and filling it in with the address
    pass

def find_nextevent():
    pass

#code for finding the address input, will eventually be moved to a function
sleep(3)
addybox = driver.find_element(By.ID, 'row-input-0')
sleep(2)
addybox.send_keys(config.address)
sleep(2)
addybox.send_keys(Keys.ENTER)
sleep(1)
addybox.send_keys(Keys.ENTER)
sleep(3)

#at this point the trash day should be loaded on screen the next step is to extract the data

next_date = driver.find_element(By.)

sleep(100)
driver.close() # kills the web browser 

#MAIN BODY OF CODE GOES HERE.


#PSU CODE, TRACKER, LINKS, STUFF
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

