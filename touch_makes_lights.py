# capactive touch detection

import time
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.1

while True:
    if cpx.touch_A1:
        cpx.pixels[5] = (255, 0, 0)
        cpx.pixels[6] = (0, 255, 0)
        cpx.pixels[7] = (0, 0, 255)
    elif cpx.touch_A2:
        cpx.pixels[7] = (255, 0, 0)
        cpx.pixels[8] = (0, 255, 0)
        cpx.pixels[9] = (0, 0, 255)
    elif cpx.touch_A3:
        cpx.pixels[8] = (255, 0, 0)
        cpx.pixels[9] = (0, 255, 0)
    elif cpx.touch_A4:
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
        cpx.pixels[2] = (0, 0, 255)
    elif cpx.touch_A5:
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
        cpx.pixels[2] = (0, 0, 255)
    elif cpx.touch_A6:
        cpx.pixels[2] = (255, 0, 0)
        cpx.pixels[3] = (0, 255, 0)
        cpx.pixels[4] = (0, 0, 255)
    elif cpx.touch_A7:
        cpx.pixels[3] = (0, 255, 0)
        cpx.pixels[4] = (0, 0, 255)
    else:
        cpx.pixels.fill((0, 0, 0))