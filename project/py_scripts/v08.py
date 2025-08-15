#unit tests for servo motor class

from time import sleep
from subsystem_classes import servo_motor

servo_wheels = servo_motor(20, 18)

def servotests():
    print("testing the servo_motor class")

    print("testing in 1")
    sleep(1)
    servo_wheels.right()
    servo_wheels.left()
    print("test over")

servotests()