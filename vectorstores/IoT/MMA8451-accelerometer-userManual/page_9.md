<a id='d2b48cec-c662-4bb2-8012-d885eea3430d'></a>

<::A blue MMA8451 accelerometer module circuit board is mounted on a white breadboard. The board has various surface-mount components, including an integrated circuit in the center. Markings on the board include "MMA8451", an arrow indicating X, Y, and Z axes, a star symbol, and several pin labels along the bottom edge: VIN, GND, I1, I2, SDA, SCL, and A. Other visible markings include "1002" on some components and "3Uo". There are two gold-colored mounting holes on the top corners of the board.
: figure::>

<a id='acdc07b9-3971-47b9-b510-755bce8e29af'></a>

<::A close-up image of a blue circuit board with various electronic components. Several integrated circuits (ICs), resistors, and capacitors are visible. Along the bottom edge of the board, there are solder points labeled from left to right: "VIN", "GND", "3V0", "I1", "I2", "SDA", "SCL", and "A". Some resistors have "1002" printed on them. There is a central black IC and smaller black ICs and other components scattered across the board.
: figure::>

<a id='c42f2496-3515-4f42-ba31-16a7b726008c'></a>

You're done! Check your solder joints visually and continue onto the next steps

<a id='684e3e7e-2bdb-45f2-9d66-c9d117078760'></a>

# Arduino Code
You can easily wire this breakout to any microcontroller, we'll be using an Arduino. For another kind of microcontroller, just make sure it has I2C with **repeated-start support**, then port the code - its pretty simple stuff!

<a id='0c1f4bea-da07-4950-879c-b76d4ebc6680'></a>

<::An image showing an Arduino Uno board connected to a white breadboard with an MMA8451 sensor module. The Arduino Uno is a blue circuit board with various components, including a USB-B port, a power jack, a large microcontroller chip, and several pin headers labeled 'DIGITAL (PWM~)', 'ANALOG IN', 'POWER', 'IOREF', and 'RESET'. The digital pins are numbered 0 through 13, and analog pins A0 through A5. Power pins include 5V, GND, and Vin. The breadboard has numbered rows from 1 to 30 and lettered columns from a to j, with power rails marked with '+' and '-' symbols along the long edges. The MMA8451 sensor module is a small blue PCB located on the breadboard, connected across rows 13 to 20 and columns f to j. It has pins labeled VIN, GND, SCL, SDA, 3V3, INT1, and INT2. The wiring connections are as follows: A red wire connects the Arduino's 5V pin to the positive power rail of the breadboard (around row 17). A black wire connects the Arduino's GND pin to the negative power rail of the breadboard (around row 18). Another red wire connects the breadboard's positive power rail (row 21) to the VIN pin of the MMA8451 module (row 20, column f). Another black wire connects the breadboard's negative power rail (row 21) to the GND pin of the MMA8451 module (row 19, column f). A green wire connects the Arduino's A4 (SDA) pin to the SDA pin of the MMA8451 module (row 14, column f). A blue wire connects the Arduino's A5 (SCL) pin to the SCL pin of the MMA8451 module (row 15, column f).: figure::>

<a id='914a5093-1e97-4648-8dc9-6d410963b74f'></a>

* Connect **Vin** to the power supply, 3-5V is fine. Use the same voltage that the microcontroller logic is based off of. For most Arduinos, that is 5V
* Connect **GND** to common power/data ground
* Connect the **SCL** pin to the I2C clock **SCL** pin on your Arduino. On an UNO & '328 based Arduino, this is also known as **A5**, on a Mega it is also known as **digital 21** and on a Leonardo/Micro, **digital 3**

<a id='e9c7bcae-9c01-4bdf-87a4-5026945d5b39'></a>

© Adafruit Industries

<a id='1957814d-5b4f-4441-a2ba-8d413681453b'></a>

Page 9 of 21