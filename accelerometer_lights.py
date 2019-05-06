# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/acceleration

import time
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.1
threshold = 4

while True:
    x, y, z = cpx.acceleration
    # print((x, y, z))
    # time.sleep(0.5)
    if x <= (-1 * threshold):
        cpx.pixels[7] = (0, 255, 0)
    else:
        cpx.pixels[7] = (0, 0, 0)
    if x >= threshold:
        cpx.pixels[2] = (0, 255, 0)
    else:
        cpx.pixels[2] = (0, 0, 0)
    if y >= threshold:
        cpx.pixels[4] = (0, 255, 0)
        cpx.pixels[5] = (0, 255, 0)
    else:
        cpx.pixels[4] = (0, 0, 0)
        cpx.pixels[5] = (0, 0, 0)
    if y <= (-1 * threshold):
        cpx.pixels[0] = (0, 255, 0)
        cpx.pixels[9] = (0, 255, 0)
    else:
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[9] = (0, 0, 0)
    if z <= (-1 * threshold):
        cpx.pixels[1] = (255, 0, 0)
        cpx.pixels[3] = (255, 0, 0)
        cpx.pixels[6] = (255, 0, 0)
        cpx.pixels[8] = (255, 0, 0)
    elif z >= threshold:
        cpx.pixels[1] = (0, 255, 0)
        cpx.pixels[3] = (0, 255, 0)
        cpx.pixels[6] = (0, 255, 0)
        cpx.pixels[8] = (0, 255, 0)
    else:
        cpx.pixels[1] = (0, 0, 0)
        cpx.pixels[3] = (0, 0, 0)
        cpx.pixels[6] = (0, 0, 0)
        cpx.pixels[8] = (0, 0, 0)