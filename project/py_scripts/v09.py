from subsystem_classes import servo_motor
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms


servo_wheels = servo_motor(20, 18)
range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])

while True:
    if range_a.distance_mm > 100:
        servo_wheels.slow_forward()
        print(range_a.distance_mm)
    else:
        print("WE'RE GONNA CRASHHHHHHHH")
        servo_wheels.stop()