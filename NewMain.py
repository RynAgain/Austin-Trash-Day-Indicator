
from random import randint
from string import whitespace
import requests, json
import re
from datetime import datetime as dt
from threading import Thread
from time import sleep as wait
import board
from neopixel import NeoPixel
from rpiAPI import PINs, BUTTs
from config import secret_key #secret key is hidden to protect my address.


#Setup for RPI NeoPixel control
num_pixels = 7 #neo pixel size
pixels = neopixel.NeoPixel(board.D18, num_pixels)

#Colors
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255,255,255)
BLACK= (0,0,0)
colours = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE, BLACK] #for possible control later.

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

def idle():
    for i in range(round(43_200/num_pixels)):
        for j in range(num_pixels):
            pixels[j] = colours[randint(0, len(colours) - 1)]
            wait(1)
        
def blink():
    for i in range(10):
        pixels.fill(RED)
        wait(1)
        pixel.fill(GREEN)
        wait(1)

def light_control():
    while True:
        rainbow_cycle(0.1)
        if recycling == True: #turn light blue
            pixels.fill(BLUE)
        else: #recycling is false #light is not blue
            blink()
        idle()


#Pixel functions
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(z):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        #pixels.show()
        wait(z)



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
