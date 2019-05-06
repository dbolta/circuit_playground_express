import math
import time
from adafruit_circuitplayground.express import cpx
from random import randint

time_sleep = 0.01
i = j = 0
j0 = i0 = 0

while True:
    while True:
        if i != i0 and i != j0:
            break
        i = randint(0, 9)
    while True:
        if j != i and j != i0 and j != j0:
            break
        j = randint(0, 9)
    cpx.pixels[i] = (randint(1, 5),
                     randint(1, 5),
                     randint(1, 5))
    cpx.pixels[j] = (randint(1, 5),
                     randint(1, 5),
                     randint(1, 5))
    time.sleep(time_sleep)
    cpx.pixels[i] = (0, 0, 0)
    cpx.pixels[j] = (0, 0, 0)
    time.sleep(time_sleep)
    i0 = i
    j0 = j
    # print(str(i)+" "+str(j))
