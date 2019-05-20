# Thanks to IRLibCP adafruit library
# https://github.com/adafruit/IRLibCP

import board
import IRLib_P07_NECxs
import time
from adafruit_circuitplayground.express import cpx

def signal_tv():
    mySend = IRLib_P07_NECxs.IRsendNECx(board.REMOTEOUT)
    Address = 0xe
    Data = 0xe040bf
    print("Sending NECx code with address={}, and data={}".format(hex(Address),hex(Data)))
    mySend.send(Data, Address)

while True:
    if cpx.switch:
        if cpx.button_a:
            signal_tv()
        if cpx.button_b:
            signal_tv()