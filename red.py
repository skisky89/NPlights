1#!/usr/bin/env python
#Lightsweeps and 'playing' withn functions
import time
#import random

from neopixel import *
LedBright = open("/home/pi/lights_ws/brightness.txt")
LED = LedBright.read()
LedBright.close()
LED = int(LED)
print(LED)

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18     # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = LED     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

def colorWipe(strip, color, wait_ms=100):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)
#Main
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
            strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
            strip.begin()
colorWipe(strip, Color(125,0,0))
