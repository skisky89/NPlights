#!/usr/bin/env python
from neopixel import *
LED_BRIGHTNESS = 191 #!/usr/bin/env python

BrightnessFile = open("/var/www/gpio/brightness.txt", "w")
BrightnessFile.write("191")
BrightnessFile.close()
