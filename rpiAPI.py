#A file for speeding up the programing of the Raspberry pi.
# I am so sick of writing these functions over and over.
#pretty sure this programed to run on ubuntu ...
import datetime
from random import randint as rng
from threading import Thread
from time import sleep as wait

import requests
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

class PINs: #class for quickly mapping and controling gpio pins on RPI
    def __init__(self, number, function) -> None:
        self.number = number
        
        self.function = function
        gpio.setup(number, gpio.OUT)

    def On_Function(self):
        gpio.output(self.number, gpio.HIGH)
        
    def Off_function(self):
        gpio.output(self.number, gpio.LOW)

class BUTTs: #button class for raspberry pi
    def __init__(self, number, function) -> None:
        self.number = number
        self.function = function
        gpio.setup(self.number, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        self.state = gpio.input(self.number)