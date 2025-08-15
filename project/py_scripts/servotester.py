"""
Sample code for servo library, demonstrating instantiation
and setting angles for a continuous servo the resulting wheel speed
of a set_duty(x) call are:

| Set duty |  Speed  | Direction |
| -------- | ------- | --------- |
|   500    | Fast    | Backward  |
|   1400   | Slow    | Backward  |
|   1500   | Stopped | None      |
|   1600   | Slow    | Forward   |
|   2500   | Fast    | Forward   |

"""
from time import sleep
from subsystem_classes import servo_motor

servo_wheels = servo_motor(20, 18)



def servotests():
    print("testing servo motor class")

    print("testing left turn in 1")
    sleep(1)
    servo_wheels.left()
    print("test over")

servotests()
