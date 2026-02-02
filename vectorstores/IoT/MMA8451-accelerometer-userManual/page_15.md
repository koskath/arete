<a id='cb6269e2-eee7-4dd2-a126-66c2cdff15a0'></a>

<::Screenshot of a "Library Manager" software window. The window features standard macOS traffic light buttons (red, yellow, green) in the top left corner. The title bar reads "Library Manager". Below the title bar, there are filter fields: "Type" with a dropdown displaying "All", "Topic" with a dropdown displaying "All", and a search input field containing the text "Adafruit_Sensor". Below these controls, a display area shows details for "Adafruit Unified Sensor by Adafruit Version 1.0.2 INSTALLED". A description reads: "Required for all Adafruit Unified Sensor based libraries. A unified sensor abstraction layer used by many Adafruit sensor libraries." At the bottom of this entry, there is a link labeled "More info".: screenshot::>

<a id='57192a38-3b08-4e09-91fe-97b57ac89478'></a>

# Python & CircuitPython
It's easy to use the MMA8451 sensor with Python or CircuitPython, and the [Adafruit CircuitPython MMA8451](https://adafru.it/C5g) module. This module allows you to easily write Python code that reads the acceleration and more from the sensor.

<a id='99c37fb4-8dec-4353-882b-651115eef4fc'></a>

You can use this sensor with any CircuitPython microcontroller board or with a computer that has GPIO and Python thanks to Adafruit_Blinka, our [CircuitPython-for-Python compatibility library](https://adafru.it/BSN).

<a id='36f50215-be1f-46b6-9635-3e6cd74adb10'></a>

# CircuitPython Microcontroller Wiring

First wire up a MMA8451 to your board exactly as shown on the previous pages for Arduino using an I2C connection. Here's an example of wiring a Feather MO to the sensor with I2C:

<a id='3acb978d-8bcc-4e9e-b750-9a9520179791'></a>

<::logo: fritzing
fritzing
The logo is a simple wordmark in a sans-serif font, all in lowercase, in a gray color.::>

<a id='50012389-19da-4911-82a1-f353e4c68d5e'></a>

Board 3V to sensor VIN
Board GND to sensor GND
Board SCL to sensor SCL
Board SDA to sensor SDA

<a id='9f25bbc8-546f-42e0-86fa-f25e7d990d9b'></a>

# Python Computer Wiring

Since there's dozens of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://adafru.it/BSN).

<a id='de00160a-e28e-4621-a124-dcf46d6415af'></a>

Here's the Raspberry Pi wired with I2C:

<a id='d1510e09-7350-441f-a886-dd7e445be3dc'></a>

© Adafruit Industries

<a id='2e3d3080-6d27-41c8-ab26-79fb320f862b'></a>

Page 15 of 21