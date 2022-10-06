#imports
from concurrent.futures import thread
import requests
import re
from datetime import datetime as dt
from threading import Thread
from time import sleep as wait
import RPi.GPIO as gpio
from rpiAPI import PINs, BUTTs


#Setup for RPI control
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#create RPI control Objects (buttons and lights)
light = PINs(26, 'Controls main light 1, on pin 26')
testbutton = BUTTs(19, 'just a button, not sure if i am going to use it.')
h1 = PINs(21, 'light on pin 21')
h2 = PINs(20, 'light on pin 20')

#Variables
next_event = '' 
recycling = False #Trash goes out every week so we just need to check for the Recycling data then
CLEANR = re.compile('<.*?>') 

#Functions
def clean_html(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def get_data(): #function for retrieving the date data and recyling data
    global next_event
    global recycling
    while True:
        url = "https://api.recollect.net/api/areas/Austin/services/waste/pages/en-US/place_calendar.json"

        querystring = {"widget_config":"{\"js_host\":\"https://api.recollect.net\",\"version\":\"0.11.1664211408\",\"api_host\":\"https://api.recollect.net\",\"third_party_cookie_enabled\":1,\"name\":\"calendar\",\"base\":\"https://recollect.net\",\"area\":\"Austin\",\"schedule_view\":1}","_":"1664844148485"}

        headers = {
            "cookie": "recollect-locale=en-US; temp-client-id=D3291396-3BFC-11ED-A651-949AB7EA60BB",
            "authority": "api.recollect.net",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "dnt": "1",
            "referer": "https://api.recollect.net/w/areas/Austin/services/323/pages/place_calendar",

            "sec-ch-ua-mobile": "?0",

            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            "x-recollect-locale": "en-US",
            "x-recollect-place": "77916FA4-DF69-11E8-8A3F-5432682931C6:323:Austin",
            "x-requested-with": "XMLHttpRequest",
            "x-widget-instance": "D3291396-3BFC-11ED-A651-949AB7EA60BB",
            "x-widget-version": "0.11.1664211408"
        }

        response = requests.request("GET", url, headers=headers, params=querystring).json()
        try:
            #print(response['sections'][1]['rows'][0]['html']) # date
            next_event = clean_html(response['sections'][1]['rows'][0]['html'])
            print(response['sections'][1]['rows'][1]['html'])
            print(response['sections'][1]['rows'][2]['html'])
            print(response['sections'][1]['rows'][3]['html'])
            recycling = True
        except:
            print(next_event)
            recycling = False
            print('No recycling this week.')
        wait(43_200) #this makes it refresh every 12 hrs

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
t1 = Thread(target=get_data)
t2 = thread(target=light_control)

#Main code
t1.start()
t2.start()

