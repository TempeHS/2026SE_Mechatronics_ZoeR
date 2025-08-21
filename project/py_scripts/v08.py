#unit tests for servo motor class

from time import sleep
from servo_classes import servo_motor

servo_wheels = servo_motor(20, 18)

def servotests():
    print("testing the servo_motor class")

    print("testing forward in 1")
    sleep(1)
    servo_wheels.fast_forward()
    print("test over")
    
    print("testing slowforward in 1")
    sleep(1)
    servo_wheels.slow_forward()
    print("test over")

    print("testing stop in 1")
    sleep(1)
    servo_wheels.stop()
    print("test over")

    print("testing backward in 1")
    sleep(1)
    servo_wheels.fast_backward()
    print("test over")

    print("testing slow backward in 1")
    sleep(1)
    servo_wheels.slow_backward()
    print("test over")

    print("testing stop (again) in 1")
    sleep(1)
    servo_wheels.stop()
    print("test over")

    print("testing right turn in 1")
    sleep(1)
    servo_wheels.right()
    print("test over")

    print("testing left turn in 1")
    sleep(1)
    servo_wheels.left()
    print("test over")

servotests()