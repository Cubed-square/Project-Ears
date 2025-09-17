"""SSD1309 demo (scroll)."""
from time import sleep
from machine import Pin, I2C  # type: ignore
from ssd1309 import Display
from picozero import Button, Pot
from xglcd_font import XglcdFont


"""Test code."""
bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
#I2C interface
i2c = I2C(0, freq=400000, scl=Pin(5), sda=Pin(4))  # Pico I2C bus1
display = Display(i2c=i2c, rst=Pin(2))
vertselect = Pot(27)

def boot():

    display.clear()
    display.draw_rectangle(0, 0, 128, 64)

    display.draw_text(3, 12, "E.A.R.S", bally)
    display.draw_text(3, 21, "FoxOS" ,bally)
    display.draw_text(3,30,"Version 1.0.0",bally)
    display.draw_text(3,39,"Codename: Red",bally)
    display.present()
    sleep(3)
    display.clear()
    
def menu():
    display.draw_rectangle(0, 0, 128, 64)
    display.draw_text(3,3,"Radio",bally, invert = False)
    display.draw_text(3,12,"Weather Report",bally, invert = False)
    display.draw_text(3,21,"System Info",bally, invert = False)
    display.draw_text(3,30,"Settings",bally, invert = False)
    display.present()


#MAINLOOP
boot()
menu()
while True:
    if vertselect.value >= .75 and vertselect.value <= 1:
        display.draw_text(3,3,"Radio",bally,invert=True)
        display.draw_text(3,12,"Weather Report",bally, invert = False)
        display.draw_text(3,21,"System Info",bally, invert = False)
        display.draw_text(3,30,"Settings",bally, invert = False)
        display.present()
    elif vertselect.value >= .50 and vertselect.value <= .74:
        display.draw_text(3,3,"Radio",bally,invert=False)
        display.draw_text(3,12,"Weather Report",bally, invert = True)
        display.draw_text(3,21,"System Info",bally, invert = False)
        display.draw_text(3,30,"Settings",bally, invert = False)
        display.present()
    elif vertselect.value >= .25 and vertselect.value <= .49:
        display.draw_text(3,3,"Radio",bally,invert=False)
        display.draw_text(3,12,"Weather Report",bally, invert = False)
        display.draw_text(3,21,"System Info",bally, invert = True)
        display.draw_text(3,30,"Settings",bally, invert = False)
        display.present()
    else:
        display.draw_text(3,3,"Radio",bally,invert=False)
        display.draw_text(3,12,"Weather Report",bally, invert = False)
        display.draw_text(3,21,"System Info",bally, invert = False)
        display.draw_text(3,30,"Settings",bally, invert = True)
        display.present()
    sleep(0.1)