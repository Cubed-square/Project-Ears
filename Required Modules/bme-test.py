from machine import I2C, Pin
import bme280

dev = I2C(scl=Pin(11), sda=Pin(10), freq=400000)
bme = bme280.BME280(i2c=dev)
print(bme.values)
