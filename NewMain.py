
import requests, json
import re
from datetime import datetime as dt
from threading import Thread
from time import sleep as wait
import RPi.GPIO as gpio
from rpiAPI import PINs, BUTTs
from config import secret_key #secret key is hidden to protect my address.


#Setup for RPI control
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#create RPI control Objects (buttons and lights)
light = PINs(26, 'Controls main light 1, on pin 26')
testbutton = BUTTs(19, 'just a button, not sure if i am going to use it.')
h1 = PINs(21, 'light on pin 21')
h2 = PINs(20, 'light on pin 20')

#Variables
next_event = '' #string for the next event
recycling = False #Trash goes out every week so we just need to check for the Recycling data then
CLEANER = re.compile('<.*?>') 

#Functions
def clean_html(raw_html):
  cleantext = re.sub(CLEANER, '', raw_html)
  return cleantext

def get_data(): #function for retrieving the date data and recycling data
    global next_event
    global recycling
    event_types = [] #list to hold what events are happening
    while True:
        try:
            url = f"https://api.recollect.net/api/places/{secret_key}/services/323"

            querystring = {"locale":"en-US"}

            headers = {
                
                "authority": "api.recollect.net",
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/json",
                "dnt": "1",
                "referer": "https://api.recollect.net/w/areas/Austin/services/323/pages/place_calendar",
                "sec-ch-ua": "^\^Chromium^^;v=^\^106^^, ^\^Google"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            r = response.json()

            next_event = r['next_event']['day']

            for i in range(len(r['next_event']['flags'])):
                event_types.append(r['next_event']['flags'][i]['name'])
            
            if 'Recycling' in event_types:
                recycling = True
            else:
                recycling = False
            print(next_event)
            print(f'Recycling is {recycling}.')

        except:
            print('Connection error.  Waiting for the next cycle to try again')
        wait(43_200) #this makes it refresh every 12 hrs
        event_types = []

def light_control():
    while True:
        if recycling == True:
            light.On_Function() #Turns on the recycling light
            h1.On_Function()
            h2.Off_function()
        else: #recycling is false
            light.Off_function()
            h1.Off_function()
            h2.On_Function()
        wait(43_200)



#Thread setup
#setting this up a multithread project allows me to go back later and enable a button control interface if i feel like it
if __name__ == '__main__':
    t1 = Thread(target=get_data)
    t2 = Thread(target=light_control)

    #Main code
    t1.start()
    wait(10)#stagger the 
    t2.start()

#Things to add:
# LCD screen control
# offline, recycling perdictions 
