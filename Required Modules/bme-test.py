import machine
import bme280

i2c = machine.I2C(sda=machine.Pin(8), scl=machine.Pin(9))
bme = bme280.BME280(i2c=i2c)
print(bme.values)
