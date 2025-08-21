#classes for the ultrasonic sensors
from machine import Pin
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

class ultrasonic_sensor:
    def __init__(self, range_a, debug = False):
        self.range_a = range_a
        self.front_sensor = PiicoDev_Ultrasonic(id=range_a)
        self.debug = debug

    def get_front(self):
        return(self.front_sensor.distance_mm)