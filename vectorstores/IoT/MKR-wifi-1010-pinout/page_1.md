<a id='7d255006-df24-483e-9db1-3259d9d846f1'></a>

<::logo: Arduino
ARDUINO
It features an infinity symbol with a minus sign on the left and a plus sign on the right, all in a light gray color.::>

<a id='1cd18851-a023-44e5-b319-21e2c4fb4a3c'></a>

ARDUINO
MKR WIFI 1010
STORE.ARDUINO.CC/MKR-WIFI-1010

<a id='2cb8a469-a667-4ca3-a324-b79432e43666'></a>

<::An illustration of a circuit board (likely an Arduino-compatible board) with a Li-Po battery connected. The board is teal colored and features various electronic components like chips, resistors, capacitors, and LEDs. A gray rectangular Li-Po 3.7 V battery is shown on the left, connected to the board via red and black wires, indicating positive (+) and negative (-) terminals. On the top edge of the board, an orange LED is labeled "Battery Charger LED" and a green LED is labeled "Power". The board has pin headers along both long sides, with numerous pins labeled for their functions.On the right side of the board, from top to bottom, the pins are labeled as follows:  - GND  - PA08 SDA  - PA09 SCL  - PA21 WK  - +5V  - LED_BUILTIN  - +5V  - VIN  - +3V3  - GND  - RESET  - D14 PB22 TX (SC5)  - D13 PB23 RX (SC5)  - ~D12 PA09 SCL (SC2)  - D11 PA08 SDA (SC2)  - ~D10 PA19 CIPO (SC1)  - D9 PA17 SCK (SC1)  - ~D8 PA16 COPI (SC1)  - ~D7 PA21  - ~D6 PA20On the left side of the board, from top to bottom, the pins are labeled as follows:  - AREF/AIN[1] PA03 AREF  - DAC0/AIN[0] PA02 A0 D15  - AIN[10] PB02 A1 D16  - AIN[11] PB03 A2 D17  - AIN[4] PA04 A3 D18~  - AIN[5] PA05 A4 D19~  - AIN[6] PA06 A5 D20  - AIN[7] PA07 A6 D21  - PA22 D0~  - PA23 D1~  - PA10 D2~  - PA11 D3~  - PB10 D4~  - PB11 D5~  : figure::>

<a id='eb0af77d-b20b-41b6-a402-a79000484ab4'></a>

Getting Started

Connecting the debugger

<::- Black square: Ground
- Red square: Power
- Teal square: LED
- Gray square: Internal Pin
- Brown square: SWD Pin
: legend::>

This is the pinout for connecting to the target device:

<::visual content::>

<a id='1e005d43-ce50-4a71-b7b6-6f7696777f97'></a>

<::Digital Pin: [Orange filled square]
Analog Pin: [Orange outlined square]
Other Pin: [White outlined square]
Microcontroller's Port: [Solid orange square]
Default: [Solid yellow square]
: legend::>

<a id='7c435dd0-5ef5-4221-90fe-de48db870305'></a>

! MAXIMUM current per pin is 7mA
! MAXIMUM source current is 46mA
! MAXIMUM sink current is 65mA per pin group

<a id='c280a8da-ad0f-43a9-805e-35e524ebced0'></a>

VIN Input voltage to the board.

NOTE: CIPO/COPI have previously
been referred to as MISO/MOSI

<a id='05bc351f-b00d-4e4b-933b-f6dae07ec7dd'></a>

<::logo: Creative Commons
CC BY SA
The logo features two interlocking 'C's, a human figure, and a circular arrow, all within rectangular and circular shapes, in a monochromatic grey scale::>