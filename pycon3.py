import math
import time
from adafruit_circuitplayground.express import cpx
from random import randint

def button_check(button_iter):
    if cpx.button_a:
        button_iter = button_iter - 1
        while True:
            if not cpx.button_a:
                break
    elif cpx.button_b:
        button_iter = button_iter + 1
        while True:
            if not cpx.button_b:
                break
    if button_iter < 0:
        button_iter = num_actions
    elif button_iter > num_actions:
        button_iter = 0
    return button_iter

button_iter = 0
num_actions = 4
#python_colors = ((32, 64, 255), (255, 180, 20))
python_colors = ((3, 6, 26), (26, 18, 2))
color_index = 0
light_ind = 0
light_ind_2 = 0
spin_colors = ((0, 20, 0), (20, 0, 0))
start = time.monotonic()

while True:
    now = time.monotonic()
    if cpx.switch:
        if cpx.button_a:
            button_iter = (button_iter - 1) % num_actions
            while True:
                if not cpx.button_a:
                    break
            cpx.pixels.fill((0, 0, 0))
        elif cpx.button_b:
            button_iter = (button_iter + 1) % num_actions
            while True:
                if not cpx.button_b:
                    break
            cpx.pixels.fill((0, 0, 0))
        # Python colors
        if button_iter == 0:
            if now - start > 0.5:
                color_index = (color_index + 1) % len(python_colors)
                cpx.pixels.fill(python_colors[color_index])
                start = now
        # spinning red and green
        if button_iter == 1:
            if now - start > 0.1:
                light_ind = (light_ind + 1) % 10
                for pixel_ind in range(10):
                    if (pixel_ind + 3) % 10 == light_ind:
                        cpx.pixels[pixel_ind] = spin_colors[0]
                    elif (pixel_ind + 2) % 10 == light_ind:
                        cpx.pixels[pixel_ind] = spin_colors[0]
                    elif (pixel_ind + 1) % 10 == light_ind:
                        cpx.pixels[pixel_ind] = spin_colors[1]
                    elif pixel_ind == light_ind:
                        cpx.pixels[pixel_ind] = spin_colors[1]
                    else:
                        cpx.pixels[pixel_ind] = (0, 0, 0)
                start = now
        # all random
        if button_iter == 2:
            if now - start > 0.1:
                light_ind = randint(0, 9)
                cpx.pixels[light_ind] = (randint(0, 5), randint(0, 5), randint(0, 5))
                start = now
        # 1 random light
        if button_iter == 3:
            if now - start > 0.06:
                cpx.pixels[light_ind] = (0, 0, 0)
                cpx.pixels[light_ind_2] = (0, 0, 0)
                light_ind = randint(0, 9)
                light_ind_2 = randint(0, 9)
                cpx.pixels[light_ind] = (randint(1, 15), randint(1, 15), randint(1, 15))
                cpx.pixels[light_ind_2] = (randint(1, 15), randint(1, 15), randint(1, 15))
                start = now
    else:
        cpx.pixels.fill((0, 0, 0))