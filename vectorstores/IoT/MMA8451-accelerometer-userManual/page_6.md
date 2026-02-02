<a id='9e79289c-7612-46a1-b391-594a22455629'></a>

## INT and ADDR Pins

*   A is the I2C Address select pin. By default this is pulled up to 3.3V with a 10K resistor, for an I2C address of 0x1D. You can also connect it to the GND pin for an address of 0x1C
*   I1 and I2 are the Interrupt #1 and #2 signal pins. These pins are for more advanced usage, where you want to be alerted by the chip say when data is ready to read, or if it detects a large motion. We don't have direct support in the example Arduino library for these pins, so please check the datasheet for the I2C commands

<a id='d8b876ed-32eb-4d45-b340-a374029569a2'></a>

Assembly
<::A top-down view of a small, square, blue circuit board (MMA8451) and a separate 8-pin male header. The circuit board has various surface-mount components, an integrated circuit, and through-hole pads labeled "VIN", "GND", "3V0", "I1", "I2", "SDA", "SCL", and "A". An X, Y, and Z axis indicator is present near the top right of the board. The pin header has eight gold-colored pins extending from a black plastic base. Both components are displayed on a dark grey background.: figure::>

<a id='054443c8-4bbc-4d50-983c-ef05c0b85a4f'></a>

<::A small, blue square circuit board with various electronic components. In the center, a black integrated circuit is visible. Several smaller components, including resistors and capacitors, are scattered across the board. Along the bottom edge, there are solder pads labeled "VIN", "3V0", "I1", "SDA", "GND", "I2", "SCL", and "A". Two mounting holes are present in the top corners. Near the top center, the text "MMA8451" is printed, accompanied by a star logo and a coordinate system with X, Y, and Z axes. The components have markings such as "1002" and "200T".: circuit board::>

<a id='33f2d908-fc6d-4b0b-a6db-3b49d549d6c1'></a>

<::A white breadboard is shown, viewed from slightly above. The breadboard has two main sections, separated by a central channel. Both the top and bottom sections feature power rails running horizontally along their edges. The top section has a red line marked with a '+' and a blue line marked with a '-' on the upper edge, and similar red and blue lines on the lower edge. The main prototyping area in both sections is marked with columns labeled 'a' through 'e' on the left side and 'f' through 'j' on the right side, with rows numbered 1 through 30 running vertically down the center. In the central channel of the breadboard, a black, 8-pin male header or integrated circuit is inserted into the holes. The numbers on the breadboard are arranged such that 1-30 are visible along the central channel, and the lettered columns are on the outer edges. The positive and negative rails are clearly marked with red and blue lines respectively, and plus and minus signs.::>

<a id='1c85103e-6c3d-4443-8d8e-a5a795e9f9df'></a>

Prepare the header strip:
Cut the strip to length if necessary. It will
be easier to solder if you insert it into a
breadboard - **long pins down**

<a id='6fef3dad-2c84-4d1f-934d-7592628d4323'></a>

©Adafruit Industries

<a id='95705c0a-2d14-486e-8bff-f5daf7d9302d'></a>

Page 6 of 21