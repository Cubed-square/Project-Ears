from machine import Pin, I2C
from time import sleep
import bme280

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

print(i2c.scan())
'''while True:
    bme = bme280.BME280(i2c=i2c)
    print(devices = i2c.scan())
    print(bme.values)
    sleep(2)'''