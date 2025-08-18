#main project file

#import all libraries/classes
from machine import Pin, PWM
#, RTC
from time import sleep
from project.lib.servo import Servo
from junk.old_subsystem_classes import servo_motor, ultrasonic_sensor

#assigning pins and other shenanigans
servo_wheels = servo_motor(20, 18)
us_sensor = ultrasonic_sensor([0, 0, 0, 0], [0, 0, 1, 0])

#rtc = RTC()
#time_last_change = rtc.datetime()

#wip main code

#will likely change the values of the servo distances later
#turn directions may be wrong, i am doing this outside of C10 and dont have the robot to check
def wall_detector():
    while True:
        us_sensor.get_range_front()
        print(f"distance from nearest object: {distance_between_two}")
        if distance_between_two < 100:
            servo_wheels.stop()
            us_sensor.get_range_side()
            if distance_between_two < 1000:
                servo_wheels.left()
            else:
                servo_wheels.right()

def green_detector():
    #this feels like something kamala would make
    #no colour sensor/lcd code yet so im just doing pseudocode for now
    #activate colour sensor function
    #if colour sensor detects green:
        #display message on lcd

def driving_in_my_car():
    while True:
        #time_now = rtc.datetime()

        servo_wheels.slow_forward()
        wall_detector()

driving_in_my_car()