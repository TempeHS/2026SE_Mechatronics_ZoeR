#the main code for the project
from servo_classes import servo_motor
from ultrasonic_classes import ultrasonic_sensor
from colour_display_classes import colour_lcd
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *
#additional imports are for bugfixing purposes - the program kept throwing a NameError for the LCD (and sometimes colour sensor)
#seems to be an inheritance/import issue, since adding these in here and in main.py fixes this (yippee!!)

LCD_screen = create_PiicoDev_SSD1306()
colour_sensor = PiicoDev_VEML6040()

servo_wheels = servo_motor(20, 18)
wall_distance = ultrasonic_sensor([0, 0, 0, 0], True)
colour_display = colour_lcd(colour_sensor, LCD_screen, False)
colour_display.green_sensor()

def main():
    while True:
        colour_display.green_sensor()
        if wall_distance.get_front() == None:
            print("")
        else:
            servo_wheels.slow_forward()
            if wall_distance.get_front() > 100:
                servo_wheels.slow_forward()
            else:
                print("Wall detected.")
                servo_wheels.stop()
                servo_wheels.right()

main()