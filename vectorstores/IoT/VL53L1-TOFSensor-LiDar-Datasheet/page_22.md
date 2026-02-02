<a id='eb1f91c7-2a6c-4440-869d-f1dbe0cfc982'></a>

Control interface

<a id='75392c5d-975c-4510-a54e-b73967fad061'></a>

VL53L1X

<a id='f80af2f0-7f25-4e61-9293-4f3aed586fcb'></a>

Figure 17. I²C timing characteristics<::timing diagram::The diagram illustrates I²C timing characteristics with two waveforms: SDA (Serial Data Line) and SCL (Serial Clock Line). Both waveforms show voltage levels relative to VIH (High-level input voltage) and VIL (Low-level input voltage).The SDA line shows 'stop' and 'start' conditions. A 'stop' condition is indicated by a rising edge on SDA while SCL is high, and a 'start' condition by a falling edge on SDA while SCL is high.The SCL line shows clock pulses.Various timing parameters are indicated:tBUF: Bus free time between a stop and start condition.tLOW: Clock low time.tR: Rise time of the signal.tHD.STA: Hold time for the start condition.tHD.DAT: Hold time for data.tF: Fall time of the signal.tHIGH: Clock high time.tSU.DAT: Setup time for data.tSU.STA: Setup time for the start condition.tSU.STO: Setup time for the stop condition.The diagram includes ellipses (...) to indicate continuation of the waveforms.All timings are measured from either VIL or VIH.::>All timings are measured from either VIL or VIH.

<a id='7e48c62c-f5ab-47e0-8bc8-a14df72da5cf'></a>

## 4.2 IC interface - reference registers
The registers shown in the table below can be used to validate the user IC interface.

<a id='9eaa93f5-fe67-48cc-a9cd-89cd407e87f1'></a>

Table 11. Reference registers
<table id="21-1">
<tr><td id="21-2">Register name</td><td id="21-3">Index</td><td id="21-4">After fresh reset, without driver loaded</td></tr>
<tr><td id="21-5">Model ID</td><td id="21-6">0x010F</td><td id="21-7">0xEA</td></tr>
<tr><td id="21-8">Module Type</td><td id="21-9">0x0110</td><td id="21-a">0xCC</td></tr>
<tr><td id="21-b">Mask Revision</td><td id="21-c">0x0111</td><td id="21-d">0x10</td></tr>
</table>

<a id='2304e17d-cb1f-4bc8-bdf8-14c50ccdff55'></a>

Note:
The I2C read/writes can be 8,16 or 32-bit. Multi-byte reads/writes are always addressed in ascending order with MSB first as shown in *Table 12*.
The customer must use the VL53L1X software driver for easy and efficient ranging operations to match performance and accuracy criteria. Hence full register details are not exposed. The customer should refer to the VL53L1X API user manual (UM2356).

<a id='0ca60893-9de5-4c94-afcf-3543476b094b'></a>

Table 12. 32-bit register example
<table id="21-e">
<tr><td id="21-f">Register address</td><td id="21-g">Byte</td></tr>
<tr><td id="21-h">Address</td><td id="21-i">MSB</td></tr>
<tr><td id="21-j">Address + 1</td><td id="21-k">..</td></tr>
<tr><td id="21-l">Address + 2</td><td id="21-m">..</td></tr>
<tr><td id="21-n">Address + 3</td><td id="21-o">LSB</td></tr>
</table>

<a id='e9f159cd-7531-4d87-a390-904e566db6f7'></a>

22/35

<a id='dd50f809-503d-4f2f-8677-daec5a42f1dd'></a>

DocID031281 Rev 3

<a id='38aa7995-7c3b-4fcb-8cea-6c9e820d1f47'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, modern font, with the "T" integrated into the "S", and a horizontal line beneath it, all in blue.::>