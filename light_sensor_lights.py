# CircuitPlaygroundExpress_LightSensor
# reads the on-board light sensor and graphs the brighness with NeoPixels
# https://learn.adafruit.com/adafruit-circuit-playground-express/playground-light-sensor

import time

import board
import neopixel
from analogio import AnalogIn
from simpleio import map_range
# from adafruit_circuitplayground.express import cpx

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=0, brightness=0.1)
pixels.fill((0, 0, 0))
pixels.show()

# cpx.pixels.brightness = 0.05

analogin = AnalogIn(board.LIGHT)

max_analog_value = 0

while True:
    if analogin.value > max_analog_value:
        max_analog_value = analogin.value

    # light value remapped to pixel position
    peak = map_range(analogin.value, 500, max_analog_value, 0, 10)
    print(analogin.value)
    print(int(peak))

    for i in range(0, 10, 1):
        if i <= peak:
            pixels[i] = (0, 25, 0) #25 is darker than 255
        else:
            pixels[i] = (0, 0, 0)
    pixels.show()