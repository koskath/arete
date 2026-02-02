<a id='1784b379-1c3e-4197-87ea-c2cc30f33d42'></a>

ARDUINODOCS

<a id='a321ef74-8552-4154-a1d6-b5d959a9d357'></a>

← Go Back

## Hardware

---

<a id='84f65b84-8d29-4fb9-8327-167b9808fe8d'></a>

MKR Connector Carrier

Tutorials
---
MKR Connector Carrier Basics
**DHT Sensor and OLED with MKR Connector Carrier**

<a id='356d0401-8260-48f9-bd3e-bde5ef5d511b'></a>

<::image of a blue circuit board labeled "MKR CONNECTOR CARRIER". The board features white connectors along its left edge labeled A0, A1, A2, A3, A4, A5, A6 (under "SERIAL"). Along its right edge, there are white connectors labeled D0, D1, D2, D3, D4, D5, D6 (under "TWI"). In the center, there are pin headers with labels including AREF, DAC0, A0-A6 on one side, and 5V, VIN, VCC, GND, RESET, TX->14, RX<-13, SCL 12, SDA 11, MISO 10, SCK 9, MOSI 8 on the other. At the bottom, a blue screw terminal block is labeled VIN, 5V, 3.3V, GND. The board also contains various integrated circuits and other electronic components.: circuit board::> The MKR Connector Carrier.

<a id='490e7fa7-241a-4a21-858e-52db72172bb4'></a>

<::Top view of a Grove DHT sensor module, showing the white sensor housing with a grid pattern and pins labeled GND, VCC, NC, SIG. The bottom view of the module shows the circuit board with various components, including capacitors, resistors, and an integrated circuit labeled '100'. There are also pins labeled GND, VCC, SDA, SCL, and NC. The module is labeled 'AOSONG AM2322'.
: figure::>
Grove DHT sensor
module.

<a id='eb47976a-8e89-4f3a-bf2a-f66a2a7552cb'></a>

We did not put a MKR board on
the Carrier, but it is required to
get the circuit to work, as
specified in the bill of materials.

<a id='943e1f46-1eb9-4e91-ac81-bde0763f9ca3'></a>

The DHT module uses a specific
pin to communicate with the MKR
board and it is mapped on D0.
This happens because the Grove
standard for digital connections
follows this rule:

<a id='7488ddae-d4d7-4b6f-a1dc-ad6c5574f149'></a>

PinFunctrionNotes

pin1 DnPrimary digital i/o
pin2 Dn+1Secondary digital i/o
pin3 VCC Power to module 5V/3.3V
pin4 GND Ground

<a id='fd58bc76-bc66-440b-8b1f-1b0af9d1b284'></a>

and the module sends SIG on pin
1 that is mapped on the primary
digital I/O.

<a id='0b227559-909a-4d3c-b421-9caf33c74eba'></a>

In the picture, the OLED module is
shown from component side to
let you see the Grove connector. It

<a id='d7a82861-e12c-4761-90f0-421f8af01d5d'></a>

ON THIS PAGE

  Hardware Required
  Circuit
  **Code**