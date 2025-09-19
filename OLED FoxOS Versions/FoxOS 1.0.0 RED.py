'''Issues
Clipping on audio playback
'''
from time import sleep
from machine import Pin, I2C, SoftI2C  # type: ignore
from ssd1309 import Display
from picozero import Button, Pot
from xglcd_font import XglcdFont
from TEA5767 import Radio


"""Test code."""
bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
#I2C interface
display = Display(i2c=I2C(0, freq=400000, scl=Pin(5), sda=Pin(4))) #initialize OLED display
radio = Radio(SoftI2C(scl=Pin(1), sda=Pin(0), freq=400000))  # initialize radio
radio.signal_adc_level = 10
vertselect = Pot(27)
btn = Button(18)
location = ""

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
    
def menuone():
    display.draw_rectangle(0, 0, 128, 64)
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

def sysinfo():
    display.clear()
    sleep(0.1)
    display.draw_rectangle(0,0,128,64)
    display.draw_text(3,3,"Hello",bally)
    display.draw_text(3,12,"Dev: Bryce",bally)
    display.draw_text(3,21,"This is a test",bally)
    display.present()
    sleep(3)
    display.clear()
    

def loadradio():
    Radio.set_frequency(radio,104.3)
    display.clear()
    display.draw_rectangle(0,0,128,64)
    display.draw_text(3,3,"Fox Radio",bally)
    display.draw_text(3,12,f"Frequency: {radio.frequency}",bally)
    display.draw_text(3,39,"Change Frequency",bally)
    display.draw_text(3,48,"Exit",bally)
    display.present()
    while True:
        if vertselect.value <= .50:
            display.draw_text(3,39,"Change Frequency",bally, invert = True)
            display.draw_text(3,48,"Exit",bally, invert = False)
        else:
            display.draw_text(3,39,"Change Frequency",bally, invert = False)
            display.draw_text(3,48,"Exit",bally, invert = True)


#MAINLOOP
boot()
while True:
    menuone()
    if btn.is_pressed:
        if vertselect.value >= .75 and vertselect.value <= 1:
            loadradio()
            break
        if vertselect.value >= .50 and vertselect.value <= .74:
            print("load weather report")
        if vertselect.value >= .25 and vertselect.value <= .49:
            sysinfo()
        if vertselect.value >= 0 and vertselect.value <= .24:
            print("load settings")
    print(vertselect.value)
    sleep(0.01)
