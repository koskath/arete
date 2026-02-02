<a id='8cfb4170-eee0-4e3a-8d67-2280252acd0f'></a>

<::A close-up photograph of a blue BME280 Pressure, Temperature, and Humidity sensor module. The module is placed on a white breadboard, with its pins inserted into the breadboard holes. The module has various components, including integrated circuits and resistors, and is labeled with "BME280", "Pressure", and "Temp+Humidity". The pins are labeled from left to right as "VIN", "3Vo", "GND", "SCK", "SDO", "SDI", and "CS".
: figure::>
You're done! Check your solder joints visually and continue onto the next steps

<a id='f021cd9a-1dfd-406f-a68c-78d97495bdb2'></a>

<::A close-up view of a small blue circuit board labeled "Temp+Humidity". The board has various surface-mount components, including resistors labeled "1002", "2001", and "2006", and an integrated circuit labeled "0133". There's also a small square component in the center that appears to be the sensor. Along the bottom edge of the board, there are solder pads with corresponding labels: "UIN", "GND", "SDO", and "CS" on the top row, and "/3Vo", "SCK/", and "SDI" on the bottom row. A small star-shaped logo is visible in the upper right corner.
: figure::>

<a id='61bf2d9b-6cfd-476b-acfc-6dcea57526bc'></a>

# Arduino Test
You can easily wire this breakout to any microcontroller, we'll be using an Arduino. For another kind of microcontroller, as long as you have 4 available pins it is possible to 'bit-bang SPI' or you can use two I2C pins, but usually those pins are fixed in hardware. Just check out the library, then port the code.

<a id='fd9f86cb-7209-4aa7-b732-2eb5bb04e684'></a>

I2C Wiring

Use this wiring if you want to connect via I2C interface

<a id='caea6a63-ef9a-496b-a1c5-b62f4a40603c'></a>

© Adafruit Industries

<a id='114a2cbe-ebac-4acf-bb85-7b51bf63798f'></a>

Page 10 of 34