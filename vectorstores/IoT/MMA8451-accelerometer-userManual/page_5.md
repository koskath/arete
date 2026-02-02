<a id='e040f59b-ee31-4b73-bfad-fcef653fd455'></a>

Pinouts

<a id='37f12efa-4235-4be9-bf4b-724f8b792555'></a>

<::A close-up overhead view of a small, rectangular blue circuit board, likely an accelerometer breakout board. The board features several surface-mount components, including a central integrated circuit, various resistors (some labeled "1002"), and capacitors. Along the bottom and left edges, there are gold-plated through-holes for connecting wires, labeled with functions: "VIN", "GND", "3V0", "I1", "I2", "SCL", "SDA", and "A". In the top center, the model number "MMA8451" is printed in white text, along with a star-shaped logo. To the right of the model number, an orthogonal coordinate system with arrows indicates the X, Y, and Z axes. There are two larger, gold-plated mounting holes in the top left and top right corners of the board. The background is a dark, textured surface.: circuit board::>

<a id='a6fe834e-a909-4e56-835b-b9e0fdde1fc3'></a>

The little chip in the middle of the PCB is the actual MMA8451 sensor that does all the motion sensing. We add all the extra components you need to get started, and 'break out' all the other pins you may want to connect to onto the PCB. For more details you can check out the schematics in the Downloads page.

<a id='f60e80e2-4ee4-48dc-9bd9-9b993ec1bef4'></a>

# Power Pins
The sensor on the breakout requires 3V power. Since many customers have 5V microcontrollers like Arduino, we tossed a 3.3V regulator on the board. Its ultra-low dropout so you can power it from 3.3V-5V just fine.
*   **Vin** - this is the power pin. Since the chip uses 3 VDC, we have included a voltage regulator on board that will take 3-5VDC and safely convert it down. To power the board, give it the same power as the logic level of your microcontroller - e.g. for a 5V micro like Arduino, use 5V
*   **3Vo** - this is the 3.3V output from the voltage regulator, you can grab up to 100mA from this if you like
*   **GND** - common ground for power and logic

<a id='326cd89a-9935-498e-893f-194c4fd19874'></a>

# I2C Pins

* SCL - I2C clock pin, connect to your microcontrollers I2C clock line.
* SDA - I2C data pin, connect to your microcontrollers I2C data line.

<a id='33b672a7-3ab6-4c86-832d-925aa07dabaa'></a>

© Adafruit Industries

<a id='88bada5a-76e7-4b41-83ac-bacfea81e43b'></a>

Page 5 of 21