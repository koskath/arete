<a id='f3fb1a64-ee98-4a00-a0d5-5be8650da304'></a>

Fab Print - STEMMA QT version

<a id='88b11199-0267-41dd-ad6b-2011f966beb0'></a>

<::A circuit board layout with dimensions. The board is rectangular with rounded corners. Various components and traces are visible in red, blue, and magenta. Several labels are printed on the board, some of which are mirrored. Around the board, dimension lines indicate measurements. The top dimension is 0.80. The left vertical dimension is 0.10. The right vertical dimensions are 0.50 and 0.70. The bottom horizontal dimension is 1.00. Labels on the board include: P$1 (twice), mirrored "BMP580", mirrored "temperature sensor", mirrored "I2C addr 0x76", mirrored "I2C addr 0x77", mirrored "VDDIO ACC 3-5VDC", and pin labels such as SCL, SDA, CSB, SDO, GND, VCC. There are also labels "16Mhz" on the right side and "2" on the left side.: figure::>

<a id='0cc09a8c-c80c-412c-9da5-6522796722d1'></a>

Schematic - Original version

<a id='4b5a36de-e5c2-4fa2-80f0-b8bd2e0152fc'></a>

Click to enlarge. BMP280 shares the same package & pinout as the BME280 so the schematic is the same

<a id='097cef43-a138-4309-8e43-d7e9d1dd5fb5'></a>

LEVEL SHIFTING (5U <--> 3U)
<::A schematic diagram showing level shifting and a voltage regulator.
- **Level Shifting Circuit:**
  - Two channels for level shifting between 3.3V and 5V. Each channel uses two pull-up resistors (to 3.3V and 5V respectively) and a BSS138 MOSFET.
  - The first channel connects "SCK/SCL 3V" to "SCK/SCL 5V".
  - The second channel connects "SDI/SDA 3V" to "SDI/SDA 5V".
  - There are also connections for "SDO/ADR 3V" and "CSB 3V" to "SDO/ADR 5V" and "CSB 5V" respectively, through pull-up resistors.
- **Voltage Regulator (U2):**
  - A MIC5225-3.3 voltage regulator with 5V input (IN) and 3.3V output (OUT).
  - The enable (EN) pin is connected to 5V.
  - Input and output capacitors are connected to ground (GND).
: schematic diagram::>
For SPI set CSB lou at startup
SDO=MISO, SDI=MOSI, SCK=SCK, CSB=CS/SSEL
For I2C leave CSB pulled high (default value)
SDI=SDA, SCK=SCL

<::A schematic diagram showing a BME280 sensor, a pin header, and document information.
- **BME280 Digital Environment Sensor (U1):**
  - Pins: VDD (connected to 3.3V), SDO (connected to SDO/ADR 3V), CSB (connected to CSB 3V), SCK (connected to SCK 3V), SDI (connected to SDI 3V), and GND.
  - Operating temperature range: -40°C to 85°C.
- **8-pin Header (JP2):**
  - Pins 1-8 are connected to 3.3V, 5V, SDO/ADR 3V, SCK/SCL 3V, SDI/SDA 3V, CSB 3V, and GND.
- **Document Footer:**
  - Logo: Adafruit
  - Filename: Adafruit_BME280_SPI_REU-B
  - Date/Time: 6/21/2015 2:19:58 PM
  - Sheet: 1/1
  - Drawing: >AUTHOR
  - Company: Adafruit Industries
: schematic diagram::>

<a id='dc1fb7b3-0fb2-4af5-97a7-0c7b6870086e'></a>

<::logo: Adafruit
adafruit
The logo features a stylized red flower symbol next to the word "adafruit" in a sans-serif font.::>

<a id='6cc22c7c-2869-44af-8d26-d9aad6daad9a'></a>

©Adafruit Industries

<a id='1fc2ea80-9d5a-4e93-8a3e-7951934f6582'></a>

Page 33 of 34