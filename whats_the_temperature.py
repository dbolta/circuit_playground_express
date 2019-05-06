import time
from adafruit_circuitplayground.express import cpx

while True:
    celsius = cpx.temperature
    fahrenheit = celsius  * 9/5 +32
    print(fahrenheit)
    time.sleep(0.5)