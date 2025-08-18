#main file for classes/libraries

import time
from machine import Pin, PWM
from project.lib.servo import Servo
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

class servo_motor:
    def __init__(self, servo_left_pin, servo_right_pin, debug = False):
        self.servo_left_pin = servo_left_pin
        self.left_wheel = Servo(PWM(Pin(servo_left_pin)))
        self.servo_right_pin = servo_right_pin
        self.right_wheel = Servo(PWM(Pin(servo_right_pin)))
        self.__debug = debug
    
    def slow_forward(self):
        if self.__debug:
            print("servo moving forward (slow)")
        self.left_wheel.set_duty(1800)
        self.right_wheel.set_duty(1200)
    
    def fast_forward(self):
        if self.__debug:
            print("servo moving forward (fast)")
        self.left_wheel.set_duty(2500)
        self.right_wheel.set_duty(500)
    
    def slow_backward(self):
        if self.__debug:
            print("servo moving backward (slow)")
        self.left_wheel.set_duty(1200)
        self.right_wheel.set_duty(1800)
    
    def fast_backward(self):
        if self.__debug:
            print("servo moving backward (fast)")
        self.left_wheel.set_duty(500)
        self.right_wheel.set_duty(2500)
    
    def right(self):
        if self.__debug:
            print("servo turning right")
            
        self.right_wheel.set_angle(0)
        time.sleep(1) 
        self.right_wheel.set_angle(90)
        time.sleep(2) 
    
    def left(self):
        if self.__debug:
            print("servo turning left")
        
        self.left_wheel.set_angle(180)
        time.sleep(1) 
        self.left_wheel.set_angle(90)
        time.sleep(2) 
    
    def stop(self):
        if self.__debug:
            print("servo stopping")
        self.left_wheel.set_duty(1500)
        self.right_wheel.set_duty(1500)

class ultrasonic_sensor:
    def __init__(self, range_a, range_b, debug = False):
        self.range_a = range_a
        self.range_b = range_b
        self.front_sensor = PiicoDev_Ultrasonic(id=range_a)
        self.side_sensor = PiicoDev_Ultrasonic(id=range_b)
        self.debug = debug

    def get_range(self):
        print(self.front_sensor.distance_mm, self.side_sensor.distance_mm)
        sleep_ms(100)

    def get_range_front(self):
        distance_between_two = (self.front_sensor.distance_mm)
        print(distance_between_two)
    
    def get_range_side(self):
        distance_between_two = (self.side_sensor.distance_mm)
        print(distance_between_two)
