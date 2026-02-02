<a id='abc12495-7146-4906-9689-b73404657fb4'></a>

Install the `Arduino SigFox for MKRFox1200` library that is available from the Library Manager, and it is also **NECESSARY** to install the `Arduino Low Power` , and the `RTCZero` libraries.

<a id='89b26c5c-d9d4-4741-806e-b81d49a195e8'></a>

## Library Manager

Type: All Topic: All
sigfox

### Arduino SigFox for MKRFox1200 by Arduino
Helper library for MKRFox1200 board and ATAB8520E Sigfox module This library allows some high level operations on Sigfox module, to ease integration with existing projects
More info

Install

### SmartEverything SIGFOX LE51-868 by Mik Version 2.1.1 INSTALLED
Library code for the TELEIT LE51-868 a SIGFOX module
The LE51-868 S is a high performance certified Short Range to Long Range module designed to cover the 863-870 MHz band working with the Telit Proprietary protocol and acting as a SIGFOX gateway.
It has high value technical characteristics such as a -126dBm sensitivity, ultra-low power consumption and up to 15.5dBm of Output power.
It is very easy to integrate, with small form factor and acts as a long range communication module connecting directly to SIGFOX network
More info

Close

<a id='c2a4b37d-42b4-4388-8ea2-4bfcd173f7b5'></a>

After a successful installation, we can now select the Board in the Arduino IDE. Just select the Arduino MKRFOX12000. Select, as with any other Arduino board, the port where de device is connected.

<a id='6e515ab3-2ecb-433e-a1cc-8e6bfe10594e'></a>

Arduino SAMD (32-bits ARM Cortex-M0+) Boards
option Arduino/Genuino Zero (Programming Port): [ ]
option Arduino/Genuino Zero (Native USB Port): [ ]
option Arduino/Genuino MKR1000: [ ]
option Arduino MKRZero: [ ]
option Arduino MKRFox1200: [x]
option Adafruit Circuit Playground Express: [ ]
option Arduino MO Pro (Programming Port): [ ]
option Arduino MO Pro (Native USB Port): [ ]
option Arduino MO: [ ]
option Arduino Tian: [ ]

<a id='aa7bd441-bbdb-45e6-90ca-9b591bc9acf8'></a>

Check that everything is up and running by flashing this example, which will provide information about the module, like the board ID and PAC. This information is necessary for registering the device in Sigfox.

<a id='2665d7d6-dee4-46d2-bd48-360183a3763d'></a>

9