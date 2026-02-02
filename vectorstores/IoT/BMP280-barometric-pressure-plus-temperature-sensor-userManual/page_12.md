<a id='4304aa11-6bf4-438b-8723-0a5d95d3e820'></a>

<:: A top-down view of a black Adafruit Metro microcontroller board connected to a white breadboard. A blue BME280 sensor module is plugged into the breadboard. Jumper wires connect the Metro board to the breadboard and the sensor module. Specifically, a red wire connects the Metro's 5V pin to the positive power rail of the breadboard, and a black wire connects the Metro's GND pin to the negative power rail. The BME280 sensor is connected to the breadboard with a red wire from the breadboard's positive rail to the sensor's VIN, a brown wire from the breadboard's negative rail to the sensor's GND, a yellow wire from the Metro's SDA pin to the sensor's SDA, a green wire from the Metro's SCL pin to the sensor's SCL, and a light blue wire from the Metro's D2 pin to the sensor's SCK. The breadboard has rows labeled 1 through 30 and columns 'a' through 'j'.
: figure::>
<:: A top-down view of a black Adafruit Metro microcontroller board connected to a smaller white breadboard. A black BME280 sensor module is plugged into the small breadboard. Jumper wires connect the Metro board to the small breadboard and the sensor module. A red wire connects the Metro's 5V pin to the sensor's VIN pin (via the breadboard), a black wire connects the Metro's GND pin to the sensor's GND pin (via the breadboard), a purple wire connects the Metro's SDA pin to the sensor's SDA pin, a green wire connects the Metro's SCL pin to the sensor's SCL pin, and a yellow wire connects the Metro's D2 pin to the sensor's SCK pin.
: figure::> 

<a id='71d18a21-9eff-4f6e-8789-6f05c07853b0'></a>

<::An image shows a blue rectangular electronic module, labeled "BMP280 Pressure Sensor" and "Adafruit Breakout", connected to a breadboard. Wires in various colors (black, red, blue, green, yellow, white) extend from the module to the breadboard, which has rows of holes for connections.::>

<a id='149d50e4-6423-4357-a048-6b5c3e04b773'></a>

Connect **Vin** to the power supply, 3V or 5V is fine. Use the same voltage that the microcontroller logic is based off of. For most Arduinos, that is 5V
Connect **GND** to common power/data ground
Connect the **SCK** pin to **Digital #13** but any pin can be used later
Connect the **SDO** pin to **Digital #12** but any pin can be used later
Connect the **SDI** pin to **Digital #11** but any pin can be used later
Connect the **CS** pin **Digital #10** but any pin can be used later

<a id='604a5c2d-e621-4165-99db-2069ce5bf0da'></a>

Later on, once we get it working, we can adjust the library to use hardware SPI if you
desire, or change the pins to other

<a id='6ae53457-434a-4e94-90fb-4ff5f8aeeb4e'></a>

# Download Adafruit_BMP280 library

To begin reading sensor data, you will need to [install the Adafruit_BMP280 library](https://adafru.it/fIK) (code on our github repository). It is available from the Arduino library manager so we recommend using that.

<a id='0c4c1ef6-d313-4eef-833a-0eb3b2b95586'></a>

From the IDE open up the library manager...<::Arduino IDE screenshot: The window title bar reads "demo | Arduino 1.8.4". The menu bar shows "File Edit Sketch Tools Help". The "Sketch" menu is open, displaying a dropdown list. The "Include Library" option is highlighted, and hovering over it reveals a sub-menu. In this sub-menu, "Manage Libraries..." is highlighted. Other options visible in the Sketch menu include: Verify/Compile Ctrl+R, Upload Ctrl+U, Upload Using Programmer Ctrl+Shift+U, Export compiled Binary Ctrl+Alt+S, Show Sketch Folder Ctrl+K, Add File.... The sub-menu for Include Library also shows: Add .ZIP Library..., Arduino libraries (header), ArduinoHttpClient, ArduinoSound, AudioZero, Bridge.::>

<a id='471525c5-09d4-4634-89d9-bc6cf9ec991a'></a>

©Adafruit Industries

<a id='65f435a8-75dc-4ea2-9d84-df1fceafb238'></a>

Page 12 of 34