<a id='7d0bcd4d-2491-4b8a-a74a-dad70baf45d9'></a>

Pinouts

<a id='a681e4f6-924d-458d-a139-9302c1c05652'></a>

<::A close-up, top-down view of a small, rectangular, black circuit board for a BMP280 Pressure Sensor. The board features various surface-mount components, including integrated circuits, resistors, and capacitors. At the top left, there's a star-like logo next to the text "BMP280 Pressure Sensor". There are four mounting holes, one in each corner, with gold-plated rings. Along the bottom edge of the board, there are seven gold-plated through-holes, labeled from left to right as: VIN, GND, SDO, CS. Above these pins, other labels are visible: 3Vo, SCK, SDI. Other text visible on the components and board includes: "on", "310", "103", "4G3P", "PS", "197", and "D1C".
: figure::>

<a id='6d6ae7ee-7596-4f6a-87ec-1b67d40b1687'></a>

<::Image of a small, square blue circuit board for a BMP280 Pressure & Temp Sensor. The board features various surface-mount electronic components, including resistors, capacitors, and integrated circuits. Text printed on the board includes 'BMP280 Pressure & Temp Sensor' at the top, and pin labels along the bottom edge: 'VIN', 'GND', 'SDO', 'CS', '3V0', 'SCK', 'SDI'. There are gold-plated circular pads below each pin label and mounting holes in the corners. A small white star logo is visible on the right side of the board.: figure::>

<a id='accf2302-4d07-4c86-b520-88ba4996d539'></a>

Power Pins:

*   **Vin** - this is the power pin. Since the sensor chip uses 3 VDC, we have included a voltage regulator on board that will take 3-5VDC and safely convert it down. To power the board, give it the same power as the logic level of your microcontroller - e.g. for a 5V micro like Arduino, use 5V
*   **3Vo** - this is the 3.3V output from the voltage regulator, you can grab up to 100mA from this if you like

<a id='5bd28799-c955-4ab4-9d6c-b0bc50a7b0e8'></a>

© Adafruit Industries

<a id='2efa8097-c6b5-44cb-8766-033c4fb3a814'></a>

Page 6 of 34