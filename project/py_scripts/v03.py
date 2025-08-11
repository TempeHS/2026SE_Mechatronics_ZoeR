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
timevar = int(0)

while timevar < 1:
    my_servo_left.set_duty(500)
    time.sleep(1.4)
    my_servo_left.set_duty(1500)
    timevar = int(timevar + 1)
    print(timevar)
    time.sleep(1)
if my_servo_left.set_duty(500):
    my_servo_left.set_duty(1500)


    #my_servo_left.set_duty(1500)
    #timevar = int(timevar + 1)
    #time.sleep(1.4)
    #my_servo_left.set_duty(1800)
    #print(timevar)
    #time.sleep(0)
#if my_servo_left.set_duty(1800):
    #my_servo_left.set_duty(1500)