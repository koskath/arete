<a id='d19949b9-4bad-4343-9b8b-a3665a0d6882'></a>

<::A circuit diagram showing a black Adafruit Feather M4 Express microcontroller board connected to a blue BMP280 Pressure & Temp Sensor module via a breadboard. The Feather M4 Express has a USB port at the bottom and multiple pin headers along its sides. The BMP280 sensor module is labeled "BMP280 Pressure & Temp Sensor" and has six pins labeled VIN, GND, SCL, SDA, 3V3, and SDO. The components are interconnected with various colored jumper wires: a green wire connects a pin on the Feather to a pin on the breadboard, a yellow wire connects from the Feather to the SCL pin of the sensor, a blue wire connects from the Feather to the SDA pin of the sensor, an orange wire connects from the Feather to the 3V3 pin of the sensor, a red wire connects from the Feather to the GND pin of the sensor, a black wire connects from the Feather to the VIN pin of the sensor, and another green wire connects from the Feather to a pin on the breadboard near the sensor. The breadboard has numbered rows and columns. The "fritzing" logo is visible in the bottom right corner of the image.
: figure::>

<a id='55af49da-b47c-4e01-aaf0-39c3b3b3fc2e'></a>

Board **3V** to sensor **VIN**
Board **GND** to sensor **GND**
Board **SCK** to sensor **SCK**
Board **MOSI** to sensor **SDI**
Board **MISO** to sensor **SDO**
Board **D5** to sensor **CS** (or use any other free digital I/O pin)

<a id='3708a84f-062e-4009-9c22-aea78057acf3'></a>

<::The image displays a circuit setup on a white breadboard. Two main electronic components are visible: an Adafruit Feather M4 microcontroller board and a BMP280 pressure sensor module. The breadboard features horizontal power rails at the top and bottom (indicated by red and blue lines) and a central prototyping area with numbered columns and lettered rows.  The Feather M4 board, positioned on the left, is a black PCB with a USB port on its left side. Its pins are labeled as follows:  - Top row (left to right): Bat, En, USB, 13, 12, 11, 10, 9, 6, 5, SCL, SDA, 3V, GND.  - Bottom row (left to right): 3V, Aref, Gnd, A0, A1, A2, A3, A4, A5, SCK, MISO, MOSI, RX, TX, D4.  The BMP280 Pressure Sensor module, located on the right side of the breadboard, is also a black PCB. Its bottom pins are labeled (from left to right): Vin, Gnd, SCL, SDA, CS, SD0.  Several colored jumper wires connect the two modules on the breadboard:  - A green wire connects the '3V' pin on the bottom row of the Feather M4 to the 'Vin' pin of the BMP280.  - A black wire connects the 'Gnd' pin on the bottom row of the Feather M4 to the 'Gnd' pin of the BMP280.  - A blue wire connects the 'SCL' pin on the bottom row of the Feather M4 to the 'SCL' pin of the BMP280.  - A purple wire connects the 'SDA' pin on the bottom row of the Feather M4 to the 'SDA' pin of the BMP280.  - Additionally, two green wires connect the Feather M4's '3V' and 'GND' pins (from its top row) to the breadboard's power rails.  The overall image shows a complete wiring diagram for connecting a BMP280 pressure sensor to an Adafruit Feather M4 microcontroller on a breadboard.::>

<a id='7a1bca69-22bf-4588-9bb6-72bce8caed72'></a>

## Python Computer Wiring

Since there's dozens of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://adafru.it/BSN).

<a id='1cb4697b-e12b-43c7-a778-e0438a8da723'></a>

Here's the Raspberry Pi wired with I2C:

<a id='1e6611ad-02f5-47b7-8354-38e82e9c60bb'></a>

©Adafruit Industries

<a id='d6863ac4-11fc-4999-b593-d53f823e5045'></a>

Page 18 of 34