from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

class Display:
    def __init__ (self, i2cChannel, sda, scl):
        # OLED setup
        sda = Pin(sda)
        scl = Pin(scl)
        i2c = I2C(i2cChannel, sda=sda, scl=scl)
        self.oled = SSD1306_I2C(128, 64, i2c)

    def showLines(self, lines):
        self.oled.fill(0)
        for i in range(len(lines)):
            self.oled.text(lines[i], 0, i*8)
        self.oled.show()
