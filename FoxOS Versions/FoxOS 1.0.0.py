import utime
import picozero
from picozero import Pot, LED
from utime import sleep
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#I2C header
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

#creating components
pot = Pot(26)
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    

def selfcheck():
  lcd.putstr("Running self checks")
  utime.sleep(1)
  lcd.backlight_off()
  utime.sleep(1)
  lcd.backlight_on()
  utime.sleep(1)
  lcd.display_off()
  utime.sleep(1)
  lcd.display_on()
  utime.sleep(1)
  lcd.clear()
  lcd.putstr("READY")
  utime.sleep(1)
  lcd.clear()

def zeropot():
    while pot.value > 0:
        lcd.putstr("Set Potentiometer to 0")
        utime.sleep(1)
        lcd.clear()


selfcheck()
zeropot()
lcd.blink_cursor_on()
lcd.clear()
scrnstate = 1
curntstate = 1
scrnlist = ["menu1","menu2","menu3","menu4"]
lcd.putstr(scrnlist[0])
while True:
    if pot.value >= 0 and pot.value < .25:
        scrnstate = 1
    elif pot.value >= .25 and pot.value < .5:
        scrnstate = 2
    elif pot.value >= .5 and pot.value < .75:
        scrnstate = 3
    elif pot.value >= .75 and pot.value <= 1:
        scrnstate = 4
    else:
        lcd.putstr("ERROR")
    if scrnstate != curntstate:
        lcd.clear()
        lcd.putstr(scrnlist[scrnstate-1])
    curntstate = scrnstate
