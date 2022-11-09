# 2022-11-08 Task 2

# Binary counter to LEDs on Arduinos

import time

from pyfirmata import Arduino

board = Arduino('/dev/cu.usbserial-120')
print("Board is ready")

while True:
    for i in range(8):
        board.digital[12].write(i // 4)
        time.sleep(1)
        board.digital[5].write((i % 4) // 2)
        time.sleep(1)
        board.digital[9].write(i % 2)
        time.sleep(1)
