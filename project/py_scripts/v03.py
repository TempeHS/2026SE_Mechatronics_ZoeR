#sample servo code/servo unit tests

import time
from machine import Pin, PWM
from servo import Servo


# create a PWM servo controller (16 - pin Pico)
servo_pwm = PWM(Pin(20))
r_servo_pwm = PWM(Pin(18))

# create a servo object
my_servo = Servo(pwm=servo_pwm)
r_my_servo = Servo(pwm=r_servo_pwm)


while True:
    # manually set the servo duty time
    my_servo.set_duty(500)
    r_my_servo.set_duty(2500)
    time.sleep(2)

    my_servo.set_duty(1500)
    r_my_servo.set_duty(1500)
    time.sleep(2)

    my_servo.set_duty(2500)
    r_my_servo.set_duty(500)
    time.sleep(2)

    my_servo.stop()
    r_my_servo.stop()
    time.sleep(2)