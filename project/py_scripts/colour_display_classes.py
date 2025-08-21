#classes for the servos/wheels
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *

display = create_PiicoDev_SSD1306()
colour_sensor = PiicoDev_VEML6040()

class colour_lcd:
    def __init__(self, colour_sensor, display, debug):
        self.colour_sensor = colour_sensor
        self.display = display
        self.__debug = debug
    
    def green_sensor(self):
        if self.__debug:
            print("checking for the colour green")
        data = self.colour_sensor.readHSV()
        hue = data["hue"]
        print(hue)

        if hue > 70 and hue < 80:
            display.poweron()
            display.text("green detected", 1, 15, 1)
            display.show()
        else:
            display.poweroff()

im_tired_boss = colour_lcd(colour_sensor, display, True)
im_tired_boss.green_sensor()
