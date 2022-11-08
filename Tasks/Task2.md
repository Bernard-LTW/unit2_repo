# Task 2

## Prompt
To build the circuit below using Arduino and create the program in Python to control the LED.

## Code Structure 
```.py
#2022-11-08 Task 2

#Binary counter to LEDs on Arduinos

from pyfirmata import Arduino
import time

board = Arduino('/dev/cu.usbserial-120')
print("Board is ready")

for i in range(8):
    board.digital[12].write(i//4)
    time.sleep(1)
    board.digital[5].write((i%4)//2)
    time.sleep(1)
    board.digital[9].write(i%2)
    time.sleep(1)
```

## Evidence
![](/Assets/Task2_Evidence.jpg)
*Fig.1* **Photo of the build**

## Video
![](https://drive.google.com/file/d/1f_uqRTZztHHKePOmN2UyAHlGDSkFtJRf/view?usp=share_link)
*Fig.2* **Video of the build**






