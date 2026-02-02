<a id='ef777c82-e488-4ac6-ab16-bac1ca8dc035'></a>

<::logo: fritzing
fritzing
The logo is a stylized wordmark in a sans-serif font, rendered in a dark gray color.::>

<a id='7fddba88-64c3-4bcf-a4c2-40535af35cd3'></a>

<::A Fritzing-style diagram shows an electronic circuit assembled on a white breadboard. Two main components are visible: an Adafruit Feather M4 Express microcontroller board on the left and a BMP280 Pressure Sensor board on the right. Both boards are black PCBs. The breadboard has red and blue power rails along the top and bottom edges, indicating positive and negative voltage lines, respectively. The Feather M4 Express board is labeled "Adafruit Feather M4 Express" and has a USB port on its left side. Key pins on the Feather M4 board include "Bat", "En", "USB", digital pins 13 through 5, "SCL", "SDA", "3V", "Gnd", analog pins A0 through A5, "SCK", "MO", "MI", "RX", "TX", and "D4". The BMP280 Pressure Sensor board is labeled "BMP280 Pressure Sensor" and has pins for "VIN", "GND", "SCL", "SDA", "CSB", and "SDO". Connections are made with jumper wires: A red wire connects the "3V" pin of the Feather M4 to the bottom red power rail of the breadboard. A black wire connects the "Gnd" pin of the Feather M4 to the bottom blue power rail. The BMP280 sensor's "VIN" pin is connected to the bottom red power rail, and its "GND" pin is connected to the bottom blue power rail. A yellow wire connects the "SDA" pin of the Feather M4 to the "SDA" pin of the BMP280. A blue wire connects the "SCL" pin of the Feather M4 to the "SCL" pin of the BMP280. This setup demonstrates an I2C communication connection between the Feather M4 and the BMP280 sensor, powered via the breadboard's rails.: circuit diagram::>

<a id='666e9974-16aa-4aff-82a7-d093287a9168'></a>

Board 3V to sensor VIN (red wire on
STEMMA version)
Board GND to sensor GND (black wire on
STEMMA version)
Board SCL to sensor SCK (yellow wire on
STEMMA version)
Board SDA to sensor SDI (blue wire on
STEMMA version)

<a id='b04aab38-49b9-4f3d-8341-ce69c18bab1d'></a>

<::A diagram showing two electronic boards connected by colored wires. On the left is a rectangular board labeled "BMP280 Pressure Sensor" with pins labeled VIN, GND, SDO, SCK, SDA, and CS. On the right is a larger rectangular board labeled "Feather M4 Express" by Adafruit. This board has a USB port, a reset button, and numerous pins labeled from 3V, Aref, Gnd, A0 to A5, SCK, MOSI, MISO, RX, TX, and D4, as well as digital pins 13 down to 5, SCL, and SDA. A black wire connects the GND pin of the sensor to a GND pin on the Feather M4. A red wire connects the VIN pin of the sensor to a 3V pin on the Feather M4. A blue wire connects the SDA pin of the sensor to the SDA pin on the Feather M4. A yellow wire connects the SCK pin of the sensor to the SCL pin on the Feather M4. The text "fritzing" is visible in the bottom right corner of the image.: diagram::>
fritzing

<a id='168e2b05-88ba-435f-9d61-ee2e1445e3cd'></a>

And an example of a Feather M0 wired with hardware SPI:

<a id='cb6dd0b7-e802-404c-95a6-da31c2ae689b'></a>

Adafruit Industries

<a id='d30732ef-025c-4671-92a8-9e5ec64691d0'></a>

Page 17 of 34