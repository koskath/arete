<a id='dadc5963-43fb-4661-9b44-5016cce95cd1'></a>

<::Fritzing diagram showing a top-down view of a Raspberry Pi 3 Model B v1.2 (© Raspberry Pi 2015) connected to a blue BME280 Pressure Temperature Humidity sensor module on a breadboard. The Raspberry Pi has various ports labeled: Power, DSI (DISPLAY), HDMI, CSI (CAMERA), Audio, Ethernet, and four USB 2.0 ports. Wires connect the Raspberry Pi's GPIO pins to the breadboard and then to the BME280 sensor module. The wires are colored red, black, orange, yellow, blue, and green.fritzing
: circuit diagram::>
<::Fritzing diagram showing a bottom-up view of a Raspberry Pi 3 Model B v1.2 (© Raspberry Pi 2015) connected to a black BME280 Pressure Sensor module on a breadboard. The Raspberry Pi has various ports labeled: Power, DSI (DISPLAY), HDMI, CSI (CAMERA), Audio, Ethernet, and four USB 2.0 ports. Wires connect the Raspberry Pi's GPIO pins to the breadboard and then to the BME280 sensor module. The wires are colored red, black, blue, purple, yellow, and green.
: circuit diagram::>

<a id='11fbaf88-77f1-4b8e-aeeb-94171aef3503'></a>

Pi **3V3** to sensor **VIN**
Pi **GND** to sensor **GND**
Pi **MOSI** to sensor **SDI**
Pi **MISO** to sensor **SDO**
Pi **SCLK** to sensor **SCK**
Pi **#5** to sensor **CS** (or use any other free
GPIO pin)

<a id='c616aff4-68f5-427a-b1bf-dd7981d4238d'></a>

CircuitPython Installation of BMP280
Library

<a id='85279730-1e4b-4d8a-af44-29674cdb59b2'></a>

You'll need to install the [Adafruit CircuitPython BMP280](https://adafru.it/COx) library on your CircuitPython board.

<a id='892bf10a-be54-40bd-8c2a-459483e4a933'></a>

First make sure you are running the [latest version of Adafruit CircuitPython](https://adafru.it/Amd) for your board.

<a id='447cef56-a7cc-4b52-bec7-62c4a65b04d7'></a>

Next you'll need to install the necessary libraries to use the hardware--carefully follow the steps to find and install these libraries from [Adafruit's CircuitPython library bundle](https://adafru.it/uap). Our CircuitPython starter guide has a [great page on how to install the library bundle](https://adafru.it/ABU).

<a id='1c16d637-2b6a-4f37-8558-d1113587636c'></a>

© Adafruit Industries

<a id='ab385b29-787a-4a54-b80f-0652dbf719db'></a>

Page 20 of 34