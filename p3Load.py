import board
import neopixel
## Load neopixel map for pind 18, 150 LEDs
pixels = neopixel.NeoPixel(board.D18, 150)

#Pixel 1 GREEN if loaded properly
pixels[0] = (0, 255, 0)
print("Loaded!")
