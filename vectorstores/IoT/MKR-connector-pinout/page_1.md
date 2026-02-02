<a id='70591fb9-a1cf-473a-a9b8-74c49ce177d1'></a>

← Go Back

Hardware

<a id='98b33cd7-bec2-4ebe-876b-deeb61d0ae33'></a>

MKR Connector Carrier

<a id='188a9176-9d71-4c2c-92a2-da2e190f5ebd'></a>

MKR Connector Carrier
Basics

DHT Sensor and OLED with
MKR Connector Carrier

<a id='a06c4623-b4c1-4526-a10c-e3b6d912aca1'></a>

Home / Hardware / MKR Connector Carrier / MKR Connector Carrier Basics

<a id='2e072eb3-6ebd-47b7-8afc-fc81e345619e'></a>

# MKR Connector Carrier Basics

Get to know your MKR Connector Carrier and learn how to connect and read sensors.

<a id='a78b6e86-4ca4-4162-9b98-021e720487c7'></a>

Author • Arduino                                                                   Last revision • 25/01/2022

<a id='de590dbd-9647-4669-80f6-40ad4cb90b92'></a>

The MKR Connector Carrier allows any MKR board to use the range of modules and devices that use the Grove Connector, developer by Seeed Studio and now a de facto standard for solderless connection of analog and digital modules.

<a id='020a30fa-94d8-43ec-833d-d47fef653aae'></a>

<::A circuit board labeled "MKR CONNECTOR CARRIER". It features various connectors and pin headers with labels. On the left side, there are vertical connectors labeled A0 through A6, with "SERIAL" written vertically near the bottom. On the right side, there are vertical connectors labeled D0 through D6, with "TWI" written vertically near the bottom. In the center, there are two rows of pin headers. The left row is labeled: AREF, DAC0, A0, A1, A2, A3, A4, A5, A6. The right row is labeled: 5V, VIN, VCC, GND, RESET, TX->14, RX<-13, SCL 12, SDA 11, MISO 10, SCK 9, MOSI 8, 7. At the bottom, there is a set of screw terminals labeled VIN, 5V, 3.3V, GND.: circuit board diagram::>

<a id='06e754a1-5f23-4973-b8fa-4cd62254a7c6'></a>

<::AD RINV-O 24-18

ARDUINO
MKR CONNECTOR
CARRIER

D0
D1
D2
D3
D4
D5
D6
TWI

5V
VIN
VCC
GND
RESET
14 TX
13 RX
12 SCL
11 SDA
10 MISO
9 SCK
8 MOSI
7
6

A0
A1
A2
A3
A4
A5
A6
SERIAL

AREF
DAC0
A0
A1
A2
A3
A4
A5
A6
0
-0
-0
-0
-0
-0

CE
ARDUINO.CC

GND 3.3V 5V VIN
: figure::>

MKR Connector Carrier bottom.

<a id='b2c18386-e285-4158-bcae-422851448099'></a>

Please note that a limited number of boards have a wrong labeling on the solder side. Please refer to the current image for the correct labelling. The component side labels are correct on all the boards. Please refer to them for your connections

<a id='65df2e1d-c25a-4c0b-9766-553675eeb350'></a>

# Power Supply
All the I/Os are supplied at 5V and the carrier provides the proper 5V to 3.3V level shifting. The board has a buck converter that can be supplied with an external voltage from 7V to 16V connected to the VIN of the screw terminal block. The buck converter supplies the MKR board that provides the 5V and the 3.3V output that can also be found on the screw terminal blocks.

<a id='d326a84a-c2ed-4085-9f50-405740543036'></a>

# Modules and Cables
The Grove modules have a standard four pins connector and usually the cable that comes with them has four standard colors:
* pin 1 - Yellow (for example, SCL on I2C Grove Connectors)
* pin 2 - White (for example, SDA on I2C Grove Connectors)
* pin 3 - Red - VCC on all Grove Connectors
* pin 4 - Black - GND on all Grove Connectors

<a id='7ccfae29-9dd0-48cf-a242-d1e60e243070'></a>

# A0-A6 Analog Input

An Grove Analog connector consists of the standard four lines coming into the Grove plug. The two signal lines are generically called A0 and A1. Most modules only use A0. Often base units will have the first connector called A0 and the second called A1 and they will be wired A0/A1 and then A1/A2, etc.

<a id='4de6a94c-456b-49a2-8fb3-14a99b4d3df8'></a>

<table id="0-1">
<tr><td id="0-2">Pin</td><td id="0-3">Function</td><td id="0-4">Notes</td></tr>
<tr><td id="0-5">pin1</td><td id="0-6">An</td><td id="0-7">Primary analog input</td></tr>
<tr><td id="0-8">pin2</td><td id="0-9">An+1</td><td id="0-a">Secondary analog input</td></tr>
<tr><td id="0-b">pin3</td><td id="0-c">VCC</td><td id="0-d">Power to module 5V/3.3V</td></tr>
<tr><td id="0-e">pin4</td><td id="0-f">GND</td><td id="0-g">Ground</td></tr>
</table>

<a id='b92e5d25-51c2-4eb2-8e64-be7a46172a76'></a>

Input only (analog or digital) with a maximum allowed voltage of 5V. The 5V to supplied the sensor is provided by the board.

<a id='d1d2451e-9a79-4fa5-80b3-da020374939a'></a>

The last connector labeled A5 A6 is a connector that wires two analog inputs into a single connector according to the grove connector specifications. If a single input has to be used the wired one is A5.

<a id='f0b3d5f0-ae1d-47d6-8707-ca097f950b1b'></a>

# D0-D6 Digital Input Output
A digital Grove connector consists of the standard four lines coming into the Grove plug. The two signal lines are generically called D0 and D1. Most modules only use D0, but some do (like the LED Bar Grove display) use both. Often base units will have the first connector called D0 and the second called D1 and they will be wired D0/D1 and then D1/D2, etc.

<a id='bb280f61-214b-4252-8b50-772b1c3e8375'></a>

<table id="0-h">
<tr><td id="0-i">Pin</td><td id="0-j">Function</td><td id="0-k">Notes</td></tr>
<tr><td id="0-l">pin1</td><td id="0-m">Dn</td><td id="0-n">Primary digital I/O</td></tr>
<tr><td id="0-o">pin2</td><td id="0-p">Dn+1</td><td id="0-q">Secondary digital I/O</td></tr>
<tr><td id="0-r">pin3</td><td id="0-s">VCC</td><td id="0-t">Power to module 5V/3.3V</td></tr>
<tr><td id="0-u">pin4</td><td id="0-v">GND</td><td id="0-w">Ground</td></tr>
</table>

<a id='6b0b4bf8-6a63-4a42-b519-b466090cdafa'></a>

I/O digital with a maximum allowed voltage of 5V. The 5V to supplied the sensor is provided by the board.
The last connector labeled D5 D6 is a connector that wires two digital I/O into a single connector according to the grove connector specifications. If a single I/O has to be used the wired one is D5.

<a id='32ca78e1-abe7-4d45-a6c3-9bfd66a8f47b'></a>

# Serial

The Serial connector on the board is wired to the MKR board according to the grove connector specifications. The Grove UART module is a specialized version of a Grove Digital Module. It uses both Pin 1 and Pin 2 for the serial input and transmit. The Grove UART plug is labeled from the base unit point of view. In other words, Pin 1 is the RX line (which the base unit uses to receive data, so it is an input) where Pin 2 is the TX line (which the base unit uses to transmit data to the Grove module).

<a id='26e86af1-0d20-493c-8320-a55e4262af17'></a>

<table><thead><tr><th>Pin</th><th>Function</th><th>Notes</th></tr></thead><tbody><tr><td>pin1</td><td>RX</td><td>Serial receive</td></tr><tr><td>pin2</td><td>TX</td><td>Serial transmit</td></tr><tr><td>pin3</td><td>VCC</td><td>Power to module 5V/3.3V</td></tr><tr><td>pin4</td><td>GND</td><td>Ground</td></tr></tbody></table>

<a id='fc518476-4e62-4432-b41b-a0fc1105a70a'></a>

# TWI - I2C

The TWI connector on the board is wired to the MKR board according to the grove connector specifications. There are many types of I2C Grove sensors available. Most are 5V/3.3V devices, but there are a few that are only 3.3V or 5.0V. You need to check the specifications.

<a id='fb38860f-6162-4d67-afbc-a0d7344a221e'></a>

The Grove I2C connector has the standard layout. Pin 1 is the SCL signal and Pin 2 is the SDA signal. Power and Ground are the same as the other connectors. This is another special version of the Grove Digital Connector. In fact, often the I2C bus on a controller (like the ESP8266, Raspberry Pi and the Arduino) just uses Digital I/O pins to implement the I2C bus. The pins on the Raspberry Pi and Arduino are special with hardware support for the I2C bus.

<a id='3b5a4c1e-038f-48b6-95a4-256add4d2d7f'></a>

<table><thead><tr><th>Pin</th><th>Function</th><th>Notes</th></tr></thead><tbody><tr><td>pin1</td><td>SCL</td><td>I2C Clock</td></tr><tr><td>pin2</td><td>SDA</td><td>I2C Data</td></tr><tr><td>pin3</td><td>VCC</td><td>Power to module 5V/3.3V</td></tr><tr><td>pin4</td><td>GND</td><td>Ground</td></tr></tbody></table>

<a id='f6932780-0b4d-47ea-8887-ee341f1d4387'></a>

## Suggest changes
The content on docs.arduino.cc is facilitated through a public GitHub repository. If you see anything wrong, you can edit this page here.

<a id='05e173e2-3e22-4610-9623-8fde13a0432e'></a>

Need support?

Help Center
Ask the Arduino Forum
Discover Arduino Discord

<a id='28d030c9-f6f8-4df6-896e-1198687d088c'></a>

# License
The Arduino documentation is licensed
under the Creative Commons Attribution-
Share Alike 4.0 license.

<a id='839a831d-9f62-4d81-816f-3a38cf2f005d'></a>

ON THIS PAGE

- **Power Supply**
  - Modules and Cables
  - A0-A6 Analog Input
  - D0-D6 Digital Input Output
  - Serial
  - TWI - I2C