#unit tests for the ultrasonic sensor class and wall avoidance code

from servo_classes import servo_motor
from ultrasonic_classes import ultrasonic_sensor
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms


servo_wheels = servo_motor(20, 18)
ultrakill = ultrasonic_sensor([0, 0, 0, 0], True)

while True:
    if ultrakill.get_front() == None:
        print("")
    else:
        print(ultrakill.get_front())
        servo_wheels.slow_forward()
        if ultrakill.get_front() > 100:
            servo_wheels.slow_forward()
        else:
            print("WE'RE GONNA CRASHHHHHHHH")
            servo_wheels.stop()
            servo_wheels.right()