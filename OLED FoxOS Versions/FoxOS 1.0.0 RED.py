'''Issues
Clipping on audio playback
'''
from time import sleep
from machine import Pin, I2C, SoftI2C, ADC  # type: ignore
from ssd1309 import Display
from picozero import Button, Pot
from xglcd_font import XglcdFont
from TEA5767 import Radio
from bme280_pico import BME280


#Defining components
bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
#I2C interface
display = Display(i2c=I2C(0, freq=400000, scl=Pin(5), sda=Pin(4))) #initialize OLED display
radio = Radio(SoftI2C(scl=Pin(1), sda=Pin(0), freq=400000))  # initialize radio
radio.signal_adc_level = 3
Radio.mute = True
vertselect = Pot(26)
btn = Button(18)
bmeaddr = I2C(1, scl=Pin(3), sda=Pin(2), freq=100000) #initialize weather sensor
sensor = BME280(bmeaddr, address=0x77)
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
    while True:
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
        if btn.is_pressed:
            if vertselect.value >= .75 and vertselect.value <= 1:
                loadradio()
                break
            if vertselect.value >= .50 and vertselect.value <= .74:
                weathereport()
                break
            if vertselect.value >= .25 and vertselect.value <= .49:
                sysinfo()
                break
            if vertselect.value >= 0 and vertselect.value <= .24:
                settings()
            sleep(0.01)

def sysinfo():
    display.clear()
    sleep(0.1)
    display.draw_rectangle(0,0,128,64)
    display.draw_text(3,3,"Build: 10/29/25",bally)
    display.draw_text(3,12,"Dev: Bryce",bally)
    display.draw_text(3,21,"Freq Band: US",bally)
    display.present()
    sleep(3)
    display.clear()

def settings():
    display.clear()
    sleep(0.1)
    display.draw_rectangle(0,0,128,64)
    display.draw_text(3,3,"Coming Soon!",bally)
    display.present()
    sleep(3)
    display.clear()

def changefreq():
    display.clear()
    sleep(1)
    display.draw_rectangle(0,0,128,64)
    while True:
        newfreq = (round((32*vertselect.value)+76,1))
        display.draw_text(3,3,f"Frequency: {newfreq}",bally)
        if btn.is_pressed:
            Radio.set_frequency(radio,newfreq)
            display.clear()
            sleep(1)
            menuone()
            break
        display.present()
        sleep(0.1)

def loadradio():
    display.clear()
    sleep(1)
    Radio.mute = False
    Radio.set_frequency(radio,101.7)
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
        if btn.is_pressed:
            if vertselect.value <= .5:
                changefreq()
            else:
                display.clear()
                sleep(1)
                menuone()
                break
        display.present()

def weathereport():
    display.clear()
    sleep(1)
    Radio.mute = True
    display.draw_rectangle(0,0,128,64)
    display.draw_text(3,3,"Snow-Fox Weather",bally)
    display.draw_text(3,12,"Temp. [C]:}",bally)
    display.draw_text(3,21,"Pres. [KPa]:",bally)
    display.draw_text(3,30,"Humi. [%]:",bally)
    display.draw_text(3,39,"Press BTN to Exit",bally, invert = True)
    display.present()
    while btn.is_pressed != True:
        t, p, h = sensor.read()
        display.draw_text(3,12,f"Temp. [C]: {round(t,2)} ",bally)
        display.draw_text(3,21,f"Pres. [KPa]: {round((p/1000),2)}",bally)
        display.draw_text(3,30,f"Humi. [%]: {round(h,2)}",bally)
        display.draw_text(3,39,"Press BTN to Exit",bally, invert = True)
        display.present()
        sleep(0.5)
    display.clear()
    sleep(1)
    


#MAINLOOP
boot()
while True:
    menuone()
