<a id='6947800f-2384-453e-9233-2290c5d581ed'></a>

Downloads

<a id='568369a2-6973-4a03-a9b6-481725f5e40e'></a>

# Documents

* Datasheet for the BMP280 sensor used in the breakout (https://adafru.it/fIO)
* Arduino BMP280 Driver (https://adafru.it/fIK)
* Fritzing object in the Adafruit Fritzing Library (https://adafru.it/Mbx)
* EagleCAD PCB files on GitHub (https://adafru.it/rDq)

<a id='6a3c6cf9-a7f7-41e0-84c5-c22f5e013add'></a>

Schematic - STEMMA QT version

<a id='cd4fc05c-b060-4ef5-94d6-d9e2d5408654'></a>

<::Schematic diagram: schematic::>
### Power supply
*   **Voltage Regulator**: MIC5219-3.3, 3.3V output, with input and output capacitors.
*   **Input/Output Pins**: VCC, GND, IN, OUT, EN, GND, P4.

### ON LED
*   **LED Circuit**: An LED with a current-limiting resistor (100 Ohm) connected to 3.3V and GND.

### I2C Pullups & Shift
*   **Level Shifting**: Two MOSFETs (BSS138) for level shifting SDA and SCL lines between 3.3V and a higher voltage (indicated by VCC).
*   **Pull-up Resistors**: Resistors pulling up SCL/SDA and SCK_3V lines to 3.3V.

### STEMMA/I2C Headers
*   **Connectors**: Two connectors (CONN051 and CONN041) with pins labeled GND, VCC, SDA, SCL, and STEMMA_I2C_QT.

### I2C Pullups
*   **Pull-up Resistors**: Resistors pulling up CS_3V, SDO/ADO, and SCL/SDA lines to 3.3V.

### BMP280 Digital Pressure Sensor
*   **Component**: BMP280 Digital Pressure Sensor with pins VDD, VIO, GND, CSB, SDO, SDI, SCL, SDA.
*   **Capacitors**: Decoupling capacitors (C19, C18).
*   **Temperature Range**: -40°C ~ +85°C.

### Additional Connector
*   **Connector J1**: Pins for VCC, SDA, SCL, SDO/ADO, CS.
<::

<::Schematic Title Block: table::>
| BMP280 rev C |
| :--- |
| **Date**: 1/15/20 13:09 |
| **Drawing**: >AUTHOR |
| **Sheet**: 1/1 |
| **Company**: Adafruit Industries |
| **Logo**: Adafruit logo (a stylized flower) |
<::

<a id='f56eae2e-6dcb-4f5d-929a-c51e44427501'></a>

© Adafruit Industries

<a id='49e6dce2-81ba-42d9-8a4f-cab9ea9aa909'></a>

Page 32 of 34