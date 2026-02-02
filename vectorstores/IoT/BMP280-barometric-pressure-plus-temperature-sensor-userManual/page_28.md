<a id='035282c3-7318-44c2-b6e9-48bc0cff62cf'></a>

For this example, set the **Send Every** interval to every 30 seconds. Don't forget to scroll down as there are 4 sensor metrics / feeds to select. On a small screen you may only see the first 3 and then wonder why altitude isn't updating (it will still be set to the default of every 15 minutes)

<a id='4a308740-c554-4a36-92c8-dfcd9318a43f'></a>

Create BMP280 Component X

Select I2C Address:
0x77

option Enable BMP280: Temperature Sensor (°C)?: [x]
Name:
BMP280: Temperature Sensor (°C)
Send Every:
Every 30 seconds

option Enable BMP280: Temperature Sensor (°F)?: [x]
Name:
BMP280: Temperature Sensor (°F)
Send Every:
Every 30 seconds

option Enable BMP280: Pressure Sensor?: [x]
Name:
BMP280: Pressure Sensor
Send Every:
Every 30 seconds

option Enable BMP280: Altitude (Relative)?: [x]
Name:

<::transcription of the content
: figure::>

← Back to Component Type

Create Component

<a id='f53e15da-a877-44a3-85f5-9c0b8911e665'></a>

Your device interface should now show the sensor components you created. After the interval you configured elapses, WipperSnapper will automatically read values from the sensor(s) and send them to Adafruit IO.

<a id='9b44afb3-7db3-4f75-9109-12333f46f5dc'></a>

©Adafruit Industries

<a id='b709ff47-f46b-4667-9284-c4a8801c6c31'></a>

Page 29 of 34