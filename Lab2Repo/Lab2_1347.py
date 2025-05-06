from machine import Pin
from neopixel import NeoPixel
import time

btn = Pin(0,pin.IN,Pin.PULL_UP)   # set GPIO48  to output to drive NeoPixel
while TRUE:
    time.sleep(.4)
    print(btn,value())             # write data to all pixels
