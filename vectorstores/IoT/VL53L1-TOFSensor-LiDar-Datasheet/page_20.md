<a id='01b8036d-b305-4c19-9037-3c5e1cf1fa4c'></a>

Control interface

<a id='2f3e27bb-7305-44b6-abfb-1b59636de6c0'></a>

VL53L1X

<a id='53b018ba-0f7b-4075-943f-d1215bb90b06'></a>

Figure 13. VL53L1X data format (write)

<::
Start
S | ADDRESS[7:0] | As | INDEX[15:8] | As | INDEX[7:0] | As | DATA[7:0] | As | P
VL53L1X acknowledges valid address
Acknowledge from VL53L1X
0x52 (write)
Stop
: chart::>

<a id='c5dd0d47-d9e2-469e-8fdd-febb2688f492'></a>

As data are received by the slave, they are written bit-by-bit to a serial/parallel register. After
each data byte has been received by the slave, an acknowledge is generated, the data are
then stored in the internal register addressed by the current index.

<a id='3b5d4c89-3b3a-4c63-b66a-8a7cb1731463'></a>

During a read message, the contents of the register addressed by the current index is read out in the byte following the device address byte. The contents of this register are parallel loaded into the serial/parallel register and clocked out of the device by the falling edge of SCL.

<a id='68e0f65b-9973-437e-90e0-3d076ff6b1a4'></a>

Figure 14. VL53L1X data format (read)

<::
0x52 (write)
S ADDRESS[7:0] As INDEX[15:8] As INDEX[7:0] As P

0x53 (read)
S ADDRESS[7:0] As DATA[7:0] Am P
: chart::>

<a id='8ff5e83d-bec8-47b4-a5e0-bf9fde90f9a4'></a>

At the end of each byte, in both read and write message sequences, an acknowledge is issued by the receiving device (that is, the VL53L1X for a write and the host for a read).

<a id='d52591db-3a6d-43a6-be45-c34cab876db0'></a>

A message can only be terminated by the bus master, either by issuing a stop condition or by a negative acknowledge (that is, **not** pulling the SDA line low) after reading a complete byte during a read operation.

<a id='8c92e2a7-995c-43be-83d0-ab2fac667e06'></a>

The interface also supports auto-increment indexing. After the first data byte has been transferred, the index is automatically incremented by 1. The master can therefore send data bytes continuously to the slave until the slave fails to provide an acknowledge or the master terminates the write communication with a stop condition. If the auto-increment feature is used the master does not have to send address indexes to accompany the data bytes.

<a id='9c0e9023-5195-4bcc-965e-16ed34cb98a4'></a>

Figure 15. VL53L1X data format (sequential write)
0x52 (write)
<table id="19-1">
<tr><td id="19-2">S</td><td id="19-3">ADDRESS[7:0]</td><td id="19-4">As</td><td id="19-5">INDEX[15:8]</td><td id="19-6">As</td><td id="19-7">INDEX[7:0]</td><td id="19-8">As</td><td id="19-9">P</td></tr>
</table>
<table id="19-a">
<tr><td id="19-b">DATA[7:0]</td><td id="19-c">As</td><td id="19-d">DATA[7:0]</td><td id="19-e">As</td><td id="19-f">DATA[7:0]</td><td id="19-g">As (element symbol)</td><td id="19-h">P (element symbol)</td></tr>
</table>

<a id='0f3c566d-1c6a-4677-ac99-d30a8bfbcf83'></a>

20/35

<a id='32d00436-e53a-498e-a2ef-48246a62b869'></a>

DocID031281 Rev 3

<a id='681fc1d8-b531-4ac6-8585-5940ba1ccf69'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold blue font, with a line underneath.::>