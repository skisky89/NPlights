#!/usr/bin/env python

BrightnessFile = open("/var/www/gpio/brightness.txt", "w")
BrightnessFile.write("128")
BrightnessFile.close()
