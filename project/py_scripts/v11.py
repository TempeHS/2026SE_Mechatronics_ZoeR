#LCD screen unit tests

from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms


display = create_PiicoDev_SSD1306()
display.text("Hello World.", 0, 0, 1)
display.show()