import time
from machine import Pin, PWM
from servo import Servo

servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(15))

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

