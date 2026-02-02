<a id='b7efe6af-3c5f-4f95-a720-9753b0b1513d'></a>

Temperature is always a floating point, in Centigrade. Pressure is a 32 bit integer with the pressure in Pascals. You may need to convert to a different value to match it with your weather report.

<a id='bc0a5eab-6d7b-4e5c-a197-68126e0a3964'></a>

It's also possible to turn the BMP280 into an altimeter. If you know the pressure at sea level, the library can calculate the current barometric pressure into altitude

<a id='5535ab08-0fae-4164-859b-ec5bb96a056d'></a>

# Python & CircuitPython Test
It's easy to use the BMP280 sensor with CircuitPython and the [Adafruit CircuitPython BMP280](https://adafru.it/COx) module. This module allows you to easily write Python code that reads the temperature and pressure from the sensor.

<a id='60ac3f64-f5cd-446d-97e3-acc27ba07dff'></a>

You can use this sensor with any CircuitPython microcontroller board or with a computer that has GPIO and Python thanks to Adafruit_Blinka, our CircuitPython-for-Python compatibility library (https://adafru.it/BSN).

<a id='9d15f5b0-69a0-4235-87a1-d03467479982'></a>

# CircuitPython Microcontroller Wiring

First wire up a BMP280 to your board exactly as shown on the previous pages for Arduino. You can use either I2C or SPI wiring, although it's recommended to use I2C for simplicity. Here's an example of wiring a Feather to the sensor with I2C:

<a id='73259469-4db1-4c49-ac34-29d2d125adbc'></a>

©Adafruit Industries

<a id='96ed7b0f-4c5a-40de-9089-18f8d28ebc46'></a>

Page 16 of 34