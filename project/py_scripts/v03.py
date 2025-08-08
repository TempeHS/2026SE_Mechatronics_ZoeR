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


import time
from machine import Pin, PWM
from servo import Servo
# from servo_classes import servo_motor

# servo_tests = servo_motor(20, 18, True)

servo_pwm = PWM(Pin(20))
servo_pwm_II = PWM(Pin(18))

my_servo_left = Servo(pwm=servo_pwm)
my_servo_right = Servo(pwm=servo_pwm_II)

while True:
    # manually set the servo duty time
    timevar = int(0)
    my_servo_right.set_duty(1200)
    time.sleep(0.5)
    my_servo_right.set_duty(1500)
    timevar = int(timevar) + 1
    print(timevar)
    time.sleep(0.5)