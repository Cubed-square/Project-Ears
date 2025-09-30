from machine import Pin, I2C
import time
import BME280 # Assuming you have the BME280 driver library uploaded to your board

# Initialize I2C communication (adjust pins and frequency as needed for your board)
# Example for ESP32:
#i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=10000) 

# Example for Raspberry Pi Pico:
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=10000)

# BME280 I2C address (usually 0x76 or 0x77)
bme = BME280.BME280(i2c=i2c, address=0x76) # Or 0x77 if yours is different

print("BME280 Sensor Demo")

while True:
    try:
        # Read sensor data
        temperature = bme.temperature
        pressure = bme.pressure
        humidity = bme.humidity

        # Print the readings
        print(f"Temperature: {temperature}")
        print(f"Pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print("-" * 20)

    except OSError as e:
        print(f"Error reading BME280 sensor: {e}")

    time.sleep(5) # Wait for 5 seconds before the next reading