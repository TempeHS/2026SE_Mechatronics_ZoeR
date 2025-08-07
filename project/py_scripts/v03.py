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


# create a PWM servo controller (16 - pin Pico)
servo_pwm = PWM(Pin(20))
servo_pwm_II = PWM(Pin(18))

# create a servo object using default servo parameters
my_servo_left = Servo(pwm=servo_pwm)
my_servo_right = Servo(pwm=servo_pwm_II)

while True:
    # manually set the servo duty time
    my_servo_right.set_duty(500)
    my_servo_left.set_duty(500)
    time.sleep(2)
    print("backwards. runs right wheel.")

#TO-DO - DOUBLE PERIOD
#FIX WIRES, RED - NEGATIVE, BLACK - POSITIVE
#TAPE WIRES IN
#TEST CODE
#GET BOTH SERVOS TO WORK AT THE SAME TIME
