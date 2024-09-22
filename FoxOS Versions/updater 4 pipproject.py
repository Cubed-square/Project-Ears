import time
import picozero
from picozero import Pot, LED, Button, pico_temp_sensor
from time import sleep
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import gc
#I2C header
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
#creating components
pota = Pot(26)
potb = Pot(27)
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
btn = Button(10)
#creating vars
scrnstate = 1
curntstate = 1
lnstate = 1
trans = True
bklight = ""
blnkcur = ""
gc.enable()
#UPDATE THIS INFORMATION #########################################################################################################
buildnumb = "1.0.4"
builddate = "9/21/2024"

def verttrav():
    global lnstate
    if potb.value >= 0 and potb.value < .25:
        lcd.move_to(19,0)
        lnstate = 1
    elif potb.value >= .25 and potb.value < .5:
        lcd.move_to(19,1)
        lnstate = 2
    elif potb.value >= .5 and potb.value < .75:
        lcd.move_to(19,2)
        lnstate = 3
    elif potb.value >= .75 and potb.value <= 1:
        lcd.move_to(19,3)
        lnstate = 4
    else:
        print("ERROR")

def hortrav():
    global scrnstate
    global trans
    global curntstate
    global scrnlist
    if pota.value >= 0 and pota.value < .25:
        scrnstate = 1
    elif pota.value >= .25 and pota.value < .5:
        scrnstate = 2
    elif pota.value >= .5 and pota.value < .75:
        scrnstate = 3
    elif pota.value >= .75 and pota.value <= 1:
        scrnstate = 4
    else:
        lcd.putstr("ERROR")
    if scrnstate != curntstate or trans == False:
        trans = True
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr(scrnlist[scrnstate-1])
        lcd.move_to(0,0)
        lcd.blink_cursor_off()
        sleep(0.5)
        lcd.blink_cursor_on()
    curntstate = scrnstate

def menucreation():
    global menua
    global menub
    global menuc
    global menud
    global bklight
    global blnkcur
    menua= "Calculator          System Settings     System Information  Voice Assistant"
    menub= "Music               Volume              Thermometer         DOOM2024"
    menuc= "Lynx                Clock               Memory List         Steel Commanders"
    menud= "Exit"
    #setting bklight and blnkcur in innit
    if lcd.backlight_on:
        bklight = "Y"
    else:
        bklight = "N"
    if lcd.blink_cursor_on:
        blnkcur = "Y"
    else:
        blnkcur = "N"
def bootscreen():
    FpartA = (0x03,0x07,0x06,0x07,0x0F,0x0C,0x1C,0x18)
    FpartB = (0x00,0x1E,0x1E,0x00,0x1C,0x1C,0x00,0x00)
    OpartA = (0x1E,0x1F,0x19,0x11,0x11,0x13,0x1F,0x0E)
    XpartA = (0x06,0x07,0x03,0x01,0x01,0x07,0x0F,0x0C)
    XpartB = (0x06,0x0E,0x0C,0x10,0x10,0x10,0x18,0x18)
    Obold = (0x0E,0x1F,0x1F,0x1B,0x1B,0x1F,0x1F,0x0E)
    Sbold = (0x1F,0x1F,0x18,0x1F,0x1F,0x03,0x1F,0x1F)
    lcd.custom_char(0,FpartA)
    lcd.custom_char(1,FpartB)
    lcd.custom_char(2,OpartA)
    lcd.custom_char(3,XpartA)
    lcd.custom_char(4,XpartB)
    lcd.custom_char(5,Obold)
    lcd.custom_char(6,Sbold)
    lcd.backlight_on()
    sleep(0.3)
    lcd.backlight_off()
    sleep(1)
    lcd.backlight_on()
    lcd.move_to(0,0)
    lcd.putstr("Booting...")
    lcd.move_to(6,1)
    for x in range(7):
        lcd.putchar(chr(x))
        lcd.move_to(7+x,1)
        sleep(.05)
    lcd.move_to(3,3)
    lcd.putstr(f"Version: {buildnumb}")
    sleep(5)
    lcd.clear()
    lcd.blink_cursor_on()
    del(FpartA)
    del(FpartB)
    del(OpartA)
    del(XpartA)
    del(XpartB)
    del(Obold)
    del(Sbold)

class apps:#APPS-------------------------------APPS-------------------------------------------------------APPS
    
    def SysInfo():
        global trans
        lcd.putstr(f"SYSTEM INFORMATION  BuildDate:{builddate} FoxOS Build {buildnumb}")
        sleep(5)
        #closing footer
        lcd.clear()
        trans = False
        mainloop()

    def Calc():
        global trans
        lcd.putstr("Welcome 2 Calculator\n")
        lcd.putstr("IN DEVELOPMENT")
        sleep(5)
        #closing footer
        lcd.clear()
        trans = False
        mainloop()
    
    def SysSettings():
        global trans
        global lnstate
        global bklight
        global blnkcur
        lcd.putstr(f"Welcome to Settings Backlight Y/N      {bklight}BlinkingCursor Y/N {blnkcur}Exit")
        while True:
            verttrav()
            if btn.is_pressed:
                if lnstate == 2 and bklight == "Y":
                    bklight = "N"
                    lcd.clear()
                    lcd.putstr(f"Welcome to Settings Backlight Y/N      {bklight}BlinkingCursor Y/N {blnkcur}Exit")
                    lcd.blink_cursor_off()
                    sleep(0.5)
                    lcd.blink_cursor_on()
                elif lnstate == 2 and bklight == "N":
                    bklight = "Y"
                    lcd.clear()
                    lcd.putstr(f"Welcome to Settings Backlight Y/N      {bklight}BlinkingCursor Y/N {blnkcur}Exit")
                    lcd.blink_cursor_off()
                    sleep(0.5)
                    lcd.blink_cursor_on()
                if lnstate == 3 and blnkcur == "Y":
                    blnkcur = "N"
                    lcd.clear()
                    lcd.putstr(f"Welcome to Settings Backlight Y/N      {bklight}BlinkingCursor Y/N {blnkcur}Exit")
                    lcd.blink_cursor_off()
                    sleep(0.5)
                    lcd.blink_cursor_on()
                elif lnstate == 3 and blnkcur == "N":
                    blnkcur = "Y"
                    lcd.clear()
                    lcd.putstr(f"Welcome to Settings Backlight Y/N      {bklight}BlinkingCursor Y/N {blnkcur}Exit")
                    lcd.blink_cursor_off()
                    sleep(0.5)
                    lcd.blink_cursor_on()
                if lnstate == 4:
                    break
        if bklight == "Y":
            lcd.backlight_on()
        elif bklight == "N":
            lcd.backlight_off()
        if blnkcur == "Y":
            lcd.blink_cursor_on()
        elif blnkcur == "N":
            lcd.blink_cursor_off()
            lcd.show_cursor()
        #closing footer
        lcd.clear()
        trans = False
        mainloop()

    def shutdown():
        lcd.clear()
        lcd.putstr("Powering down...")
        sleep(3)
        lcd.backlight_off()
        lcd.display_off()

    def thermometer():
        global trans
        lcd.clear()
        temper = pico_temp_sensor.temp
        lcd.putstr(f"The temperature is  {str(round(temper))} C")
        sleep(5)
        lcd.clear()
        trans = False
        mainloop()
    
    def taskman():
        global trans
        lcd.clear()
        memfree = str(round((gc.mem_free()/1000)))
        memalloc = str(round((gc.mem_alloc()/1000)))
        lcd.putstr(f"MEMFREE: {memfree}KB")
        lcd.move_to(0,1)
        lcd.putstr(f"MEMALLOC: {memalloc}KB")
        sleep(5)
        lcd.clear()
        trans = False
        mainloop()
    def check(): #Checks when button is pressed to see which function to call
        global lnstate
        global scrnstate
        if (scrnstate-1) == 0: #MENU 1
            if (lnstate-1) == 2:
                apps.SysInfo()
            elif (lnstate-1) == 1:
                apps.SysSettings()
            elif (lnstate-1) == 0:
                apps.Calc()
        if (scrnstate-1) == 1: #MENU 2
            if(lnstate-1) == 2:
                apps.thermometer()
        if (scrnstate-1) == 2: #MENU 3
            if (lnstate-1) == 2:
                apps.taskman()
        if (scrnstate-1) == 3: # MENU 4
            if (lnstate-1) == 0:
                apps.shutdown()

#Initialization checklist
bootscreen()
del(bootscreen)
menucreation()
scrnlist = [menua,menub,menuc,menud]
lcd.putstr(scrnlist[0])
lcd.move_to(0,0)


def mainloop():
    global scrnstate
    global curntstate
    global lnstate
    global trans
    while True:
        hortrav()
        verttrav()
        if btn.is_pressed:
            lcd.clear()
            apps.check()
            save = scrnstate
            break
        gc.collect()
mainloop()