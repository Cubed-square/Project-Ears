"""SSD1309 demo (scroll)."""
from time import sleep
from machine import Pin, I2C  # type: ignore
from ssd1309 import Display
from xglcd_font import XglcdFont


"""Test code."""
bally = XglcdFont('fonts/Bally7x9.c', 7, 9)

#spi = SPI(2, baudrate=10000000, sck=Pin(12), mosi=Pin(11))  # Lolin S3 SPI2
#display = Display(spi, dc=Pin(16), cs=Pin(10), rst=Pin(18))
# spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(13))  # ESP32 SPI1
# display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2))
i2c = I2C(0, freq=400000, scl=Pin(5), sda=Pin(4))  # Pico I2C bus1
display = Display(i2c=i2c, rst=Pin(2))

def test():

    display.clear()
    display.draw_rectangle(0, 0, 128, 64)

    display.draw_text(42, 12, "FoxOS", bally)
    display.draw_text(40, 21, "E.A.R.S" ,bally)
    display.present()

test()