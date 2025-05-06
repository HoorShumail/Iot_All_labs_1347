from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(48, Pin.OUT)  # Change this if needed
np = NeoPixel(pin, 1)

def test_rgb():
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255), (0, 0, 0)]
    for color in colors:
        np[0] = color
        np.write()
        print(f"LED set to: {color}")
        time.sleep(1)

test_rgb()