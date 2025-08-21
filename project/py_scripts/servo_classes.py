#classes for the servos/wheels
import time
from machine import Pin, PWM
from servo import Servo

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