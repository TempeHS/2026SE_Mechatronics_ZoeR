#unit tests for the colour sensors (and LCD)

from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *

colourSensor = PiicoDev_VEML6040()
display = create_PiicoDev_SSD1306()

#finally figured out how to work this thing
while True:
    data = colourSensor.readHSV()
    hue = data["hue"]
    if hue > 70 and hue < 80:
        display.text("why he oreen",1,15, 1)
        display.show()
    else:
        display.text("no green... smh",1,15, 1)
        display.show()
    