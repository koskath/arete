<a id='16d24f0c-fa97-4443-a89a-3dffb6729dc4'></a>

Here's a starting example that will print out the temperature, pressure and altitude every 2 seconds:

<a id='9a6a0536-8b99-4910-b86e-1767fa1b03a5'></a>

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simpletest Example that shows how to get temperature,
pressure, and altitude readings from a BMP280"""
import time
import board

# import digitalio # For use with SPI
import adafruit_bmp280

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C() # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a
# microcontroller
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# OR Create sensor object, communicating over the board's default SPI bus
# spi = board.SPI()
# bmp_cs = digitalio.DigitalInOut(board.D10)
# bmp280 = adafruit_bmp280.Adafruit_BMP280_SPI(spi, bmp_cs)

# change this to match the location's pressure (hPa) at sea level
bmp280.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    time.sleep(2)

<a id='a8a582af-d44e-44b3-acfa-84ddf4486354'></a>

Python Docs

<a id='033b2137-1235-4d6b-aa27-fc0458da9ee3'></a>

[Python Docs](https://adafru.it/C0B)

<a id='fbed7686-b689-4e9d-8bbb-c053dda72b83'></a>

© Adafruit Industries

<a id='3d585c5d-7b1d-4255-b558-18506bc5ec7f'></a>

Page 23 of 34