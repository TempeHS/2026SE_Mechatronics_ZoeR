#basic blink program
#also used as a unit test to make sure the robot is connected properly

from machine import Pin
from utime import sleep


pin = Pin("LED", Pin.OUT)

while True:
    pin.toggle()
    sleep(1)  # sleep 1sec
    print("LED is ON" if pin.value() else "LED is OFF")
