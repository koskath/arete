<a id='7aaa2926-f4a4-4d80-a9a9-d4cb232dee6f'></a>

<::A blue rectangular PCB (Printed Circuit Board) with various electronic components, labeled "MMA8451", "VIN", "3V0", "I1", "SDA", "GND", "I2", "SCL", and "A". It also shows x, y, z axis labels. Next to it is an 8-pin male header.
: figure::>

<a id='a66fb004-be97-4cb3-a359-6d3e8453fb15'></a>

<::A close-up image of a small blue circuit board, labeled 'MMA8451' prominently in white text near the top center. The board features various surface-mount components, including an integrated circuit chip in the center with text that appears to be '451J'. Around the chip are several smaller rectangular components, some labeled '1002'. In the top right corner, there is a white graphic indicating X, Y, and Z axes with arrows. Along the bottom edge of the board, there are solder pads or pin headers labeled from left to right: 'GND', 'VIN', '3V3', 'I1', 'I2', 'SDA', 'SCL', and 'A'. There are also mounting holes in each corner of the board.
: figure::>

<a id='3c80d188-ccdb-4e73-8359-e8fad4617512'></a>

This sensor communicates over I2C so you can share it with a bunch of other sensors on the same two I2C pins. There's an address selection pin so you can have accelerometers share an I2C bus. Please note this chip requires repeated-start I2C support (in case you are looking to port this to another processor)

<a id='98d736db-5dbe-49e8-83e0-e82dee62ebf7'></a>

<::A small blue circuit board, labeled "adafruit! 3-Axis 14-Bit Accelerometer", with specifications "±2/±4/±8g" and "5V Safe". It has two mounting holes at the top and eight circular solder pads at the bottom. The circuit board is placed next to a US quarter coin, showing the obverse side with George Washington's profile, and the text "LIBERTY", "IN GOD WE TRUST", "1998", and "P" (mint mark). This visual compares the size of the accelerometer to the quarter.
: figure::>

<a id='20c6a992-d426-4d18-9a7e-53c3653a0543'></a>

<::A blue circuit board with white text and gold-colored circular pads.The text reads:adafruit!3-Axis 14-BitAccelerometer±2/±4/±8g5V SafeThere are 8 circular pads along the bottom edge and two larger circular pads near the top corners.: figure::>

<a id='b9d88452-7928-43cb-9536-b51c7eb135d6'></a>

To get you going fast, we spun up a breakout board for this little guy. Since it's a 3V sensor, we add a low-dropout 3.3V regulator and level shifting circuitry on board. That means its perfectly safe for use with 3V or 5V power and logic.

<a id='68195183-fdcc-44db-ab6a-de8f1cadcfef'></a>

© Adafruit Industries

<a id='e330803e-b1b1-463b-9d93-e8a6d32f3b18'></a>

Page 4 of 21