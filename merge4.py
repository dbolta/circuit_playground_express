# https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/_modules/adafruit_circuitplayground/express.html
import math
import time
from adafruit_circuitplayground.express import cpx
from random import randint

from simpleio import map_range

button_iter = 0
num_actions = 7
#python_colors = ((32, 64, 255), (255, 180, 20))
python_colors = ((3, 6, 26), (26, 18, 2))
color_index = 0
light_ind = 0
light_ind_2 = 0
spin_colors = ((0, 20, 0), (20, 0, 0))
start = time.monotonic()

sin_bright = 0
sin_pix = 0
sin_slope = 1

### brightness meter
max_light_reading = 0

### accelerometer
accel_threshold = 5
accel_brightness = 15

while True:
    now = time.monotonic()
    if cpx.switch:
        if cpx.button_a:
            button_iter = (button_iter - 1) % num_actions
            while True:
                if cpx.button_b:
                    cpx.play_file("arnie.wav")
                if not cpx.button_a:
                    break
            cpx.pixels.fill((0, 0, 0))
        elif cpx.button_b:
            button_iter = (button_iter + 1) % num_actions
            while True:
                if cpx.button_a:
                    cpx.play_file("arnie.wav")
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
                r = randint(0, 15)
                g = randint(0, 15 - r)
                b = 15 - r - g
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
        if button_iter == 4:
            if now - start > 0.1:
                if abs(sin_bright) > 10:
                    sin_slope *= -1
                sin_bright += sin_slope
                if sin_bright == 0 and sin_slope > 0:
                    cpx.pixels[sin_pix] = (0, 0, 0)
                    sin_pix = (sin_pix + 1) % 10
                elif sin_bright >= 0:
                    cpx.pixels[sin_pix] = (sin_bright, 0, 0)
                else:
                    cpx.pixels[sin_pix] = (0, abs(sin_bright), 0)
                start = now
        if button_iter == 5:
            if time.monotonic() % 30 == 0:
                max_light_reading = 0
            if now - start > 0.1:
                brightness = cpx.light
                if brightness > max_light_reading:
                    max_light_reading = brightness
                peak = map_range(brightness, 0, max_light_reading, 0, 10)
                for i in range(0, 10, 1):
                    if i <= peak:
                        cpx.pixels[i] = (0, 15, 0) #25 is darker than 255
                    else:
                        cpx.pixels[i] = (1, 0, 0)
                start = now
        if button_iter == 6:
            if now - start > 0.1:
                x, y, z = cpx.acceleration
                if x <= (-1 * accel_threshold):
                    cpx.pixels[7] = (0, accel_brightness, 0)
                else:
                    cpx.pixels[7] = (0, 0, 0)
                if x >= accel_threshold:
                    cpx.pixels[2] = (0, accel_brightness, 0)
                else:
                    cpx.pixels[2] = (0, 0, 0)
                if y >= accel_threshold:
                    cpx.pixels[4] = (0, accel_brightness, 0)
                    cpx.pixels[5] = (0, accel_brightness, 0)
                else:
                    cpx.pixels[4] = (0, 0, 0)
                    cpx.pixels[5] = (0, 0, 0)
                if y <= (-1 * accel_threshold):
                    cpx.pixels[0] = (0, accel_brightness, 0)
                    cpx.pixels[9] = (0, accel_brightness, 0)
                else:
                    cpx.pixels[0] = (0, 0, 0)
                    cpx.pixels[9] = (0, 0, 0)
                if z <= (-1 * accel_threshold):
                    cpx.pixels[1] = (accel_brightness, 0, 0)
                    cpx.pixels[3] = (accel_brightness, 0, 0)
                    cpx.pixels[6] = (accel_brightness, 0, 0)
                    cpx.pixels[8] = (accel_brightness, 0, 0)
                elif z >= accel_threshold:
                    cpx.pixels[1] = (0, accel_brightness, 0)
                    cpx.pixels[3] = (0, accel_brightness, 0)
                    cpx.pixels[6] = (0, accel_brightness, 0)
                    cpx.pixels[8] = (0, accel_brightness, 0)
                else:
                    cpx.pixels[1] = (0, 0, 0)
                    cpx.pixels[3] = (0, 0, 0)
                    cpx.pixels[6] = (0, 0, 0)
                    cpx.pixels[8] = (0, 0, 0)
                start = now
    else:
        cpx.pixels.fill((0, 0, 0))