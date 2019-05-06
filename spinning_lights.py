# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/acceleration

import time
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.1

level = 25

while True:
    for which_green in range(0, 11, 1):
        #0 - 9
        #1 - 8
        #9 - 0
        #10 - na
        which_red = 9 - which_green
        for i in range(0, 10, 1):
            if i == which_green or i + 1 == which_green:
                g = level
            else:
                g = 0
            if i == which_red or i - 1 == which_red:
                r = level
            else:
                r = 0
            cpx.pixels[i] = (r, g, 0)
        #time.sleep(0.5)