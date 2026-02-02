<a id='487479da-0f9b-45db-8027-b94b174629c8'></a>

VL53L1X

<a id='d72c57e4-76fb-48a8-8ec8-3e78e8708286'></a>

Control interface

<a id='6c12a7ad-a3e2-4ed8-93f3-561c8c8715c1'></a>

## 4 Control interface

This section specifies the control interface. The I2C interface uses two signals: the serial data line (SDA) and serial clock line (SCL). Each device connected to the bus uses a unique address and a simple master/slave relationships exists.

<a id='5835f05b-d260-4a25-906a-eb47b13687f9'></a>

Both SDA and SCL lines are connected to a positive supply voltage using pull up resistors located on the host. Lines are only actively driven low. A high condition occurs when the lines float and the pull up resistors pull them up. When no data are transmitted both lines are high.

<a id='56b4d91d-37e1-4d64-bc30-f5f6fdd31cd7'></a>

Clock signal (SCL) generation is performed by the master device. The master device initiates data transfer. The I2C bus on the VL53L1X has a maximum speed of 400 kbits/s and uses a device address of 0x52.

<a id='69475f21-3281-43b1-bfc0-0052ddc861b7'></a>

Figure 11. Data transfer protocol
<::timing diagram::
This timing diagram illustrates a data transfer protocol, likely I2C, showing the interaction between SDA (Serial Data) and SCL (Serial Clock) lines.

Key elements:
- **SDA line**: Shows data transitions.
- **SCL line**: Shows clock pulses.

Sections of the protocol:
1.  **Start condition (S)**: Indicated by a high-to-low transition on SDA while SCL is high.
2.  **Address or data byte**: A sequence of 8 bits transmitted, synchronized by 8 clock pulses on SCL. The first bit is labeled MSB (Most Significant Bit), and the eighth bit is labeled LSB (Least Significant Bit). The SCL clock pulses are numbered 1 through 8.
3.  **Acknowledge (Ac/Am)**: After the 8 data bits, a 9th clock pulse occurs. During this pulse, the receiving device acknowledges by pulling the SDA line low.
4.  **Stop condition (P)**: Indicated by a low-to-high transition on SDA while SCL is high.

The diagram uses arrows to point to the "Start condition" and "Acknowledge" events, and a box around the 8-bit data transfer labeled "Address or data byte".
::>

<a id='d310e31c-bbad-4d24-b6f6-53267f8d5f5e'></a>

Information is packed in 8-bit packets (bytes) always followed by an acknowledge bit, Ac for VL53L1X acknowledge and Am for master acknowledge (host bus master). The internal data are produced by sampling SDA at a rising edge of SCL. The external data must be stable during the high period of SCL. The exceptions to this are start (S) or stop (P) conditions when SDA falls or rises respectively, while SCL is high.

<a id='bed87642-f187-413f-ae54-97c5a2ecb6fa'></a>

A message contains a series of bytes preceded by a start condition and followed by either a stop or repeated start (another start condition but without a preceding stop condition) followed by another message. The first byte contains the device address (0x52) and also specifies the data direction. If the least significant bit is low (that is, 0x52) the message is a master-write-to-the-slave. If the LSB is set (that is, 0x53) then the message is a master-read-from-the-slave.

<a id='6b9f9acb-8b44-47ce-a0c1-92db00c823f8'></a>

Figure 12. VL53L1X I²C device address: 0x52
MSBit
LSBit
<table id="18-1">
<tr><td id="18-2">0</td><td id="18-3">1</td><td id="18-4">0</td><td id="18-5">1</td><td id="18-6">0</td><td id="18-7">0</td><td id="18-8">1</td><td id="18-9">R/W</td></tr>
</table>

<a id='333713d9-ba06-48d9-b905-1fe8eefbee4e'></a>

All serial interface communications with the camera module must begin with a start condition. The VL53L1X module acknowledges the receipt of a valid address by driving the SDA wire low. The state of the read/write bit (LSB of the address byte) is stored and the next byte of data, sampled from SDA, can be interpreted. During a write sequence, the second byte received provides a 16-bit index which points to one of the internal 8-bit registers.

<a id='954d50bd-006f-47b0-9484-e32dab7ac0c3'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='1c494f03-dffd-4d7c-bc72-aba18a3a2f76'></a>

DocID031281 Rev 3

<a id='eef2b108-d44d-4da4-b86c-4be10b7fcf9d'></a>

19/35