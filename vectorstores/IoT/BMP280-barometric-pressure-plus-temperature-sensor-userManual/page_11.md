<a id='73558cd5-18ad-4557-83a0-dab24d972cb4'></a>

<::A photograph showing an Adafruit Metro microcontroller board connected to a white breadboard. The Metro board is black with "Metro" and "adafruit" logos. Wires (red, blue, yellow, black) connect the Metro board to a small blue sensor module on the breadboard, which is labeled with rows and columns.
: figure::>
<::A Fritzing diagram illustrating the wiring connections between an Adafruit Metro microcontroller board and a BMP280 pressure sensor module. The Metro board is black and labeled "Metro" and "adafruit". The sensor module is also black and connected to a small virtual breadboard area. Wires (yellow, blue, red, black) connect the two components.
: diagram::>
<::A Fritzing diagram, similar to the previous one, showing the wiring between an Adafruit Metro microcontroller board and a BMP280 pressure sensor. The Metro board is black with "Metro" and "adafruit" logos and pin labels like "Digital" and "Analog In". The sensor module is black and labeled "BMP280 Pressure Sensor". Wires (yellow, blue, red, black) connect the boards.
: diagram::>
fritzing

<a id='d9cb6b7f-cf20-4dd2-876b-9992a3810382'></a>

Connect Vin (**red wire on STEMMA**
version) to the power supply, 3-5V is fine.
Use the same voltage that the
microcontroller logic is based off of. For
most Arduinos, that is 5V
Connect GND (**black wire on STEMMA**
version) to common power/data ground
Connect the SCK (**yellow wire on STEMMA**
version) pin to the I2C clock **SCL** pin on
your Arduino. On an UNO & '328 based
Arduino, this is also known as **A5**, on a
Mega it is also known as **digital 21** and on
a Leonardo/Micro, **digital 3**
Connect the SDI (**blue wire on STEMMA**
version) pin to the I2C data **SDA** pin on
your Arduino. On an UNO & '328 based
Arduino, this is also known as **A4**, on a
Mega it is also known as **digital 20** and on
a Leonardo/Micro, **digital 2**

<a id='20ba5f1d-153e-48a0-be17-165d5853500f'></a>

## SPI Wiring

Since this is a SPI-capable sensor, we can use hardware or 'software' SPI. To make wiring identical on all Arduinos, we'll begin with 'software' SPI. The following pins should be used:

<a id='69eb1ca0-1279-405a-971b-9da985ede455'></a>

© Adafruit Industries

<a id='04c077d9-c482-4c65-a2ca-de02b4cdd060'></a>

Page 11 of 34