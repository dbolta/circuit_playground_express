import math
import time
from adafruit_circuitplayground.express import cpx
import simpleio

time_sleep = 0.1
i = 0
period = 0.2
max_brightness = 5
j0 = 0

while True:
    j = time.monotonic() % period

    if j < j0:
        for k in range(0, 10, 1):
            cpx.pixels[k] = (0, 0, 0)
        i += 1
        if i > 9:
            i = 0

    if cpx.switch:
        b = simpleio.map_range(j,
                               0, period, 0, 628318) / 100000
        b = -1 * math.sin(b)
        brightness = simpleio.map_range(abs(b),
                                        0, 1, 0, max_brightness)
        brightness = round(brightness)
        if b >= 0:
            cpx.pixels[i] = (0, brightness, 0)
        elif b < 0:
            cpx.pixels[i] = (brightness, 0, 0)
        #print(j)
        #time.sleep(time_sleep)
    else:
        for k in range(0, 10, 1):
            cpx.pixels[k] = (0, 0, 0)
    j0 = j
