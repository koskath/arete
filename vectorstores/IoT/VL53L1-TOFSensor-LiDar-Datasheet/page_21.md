<a id='3f0bb5aa-66fe-4a2f-8546-0ced453f0a6c'></a>

VL53L1X

<a id='c1db8d04-953a-4ecc-872c-d76812131111'></a>

Control interface

<a id='7f77cd2c-bc80-480d-91d7-a09a25b5cbc5'></a>

Figure 16. VL53L1X data format (sequential read)
0x52 (write)
<table id="20-1">
<tr><td id="20-2">S</td><td id="20-3">ADDRESS[7:0]</td><td id="20-4">As</td><td id="20-5">INDEX[15:8]</td><td id="20-6">As</td><td id="20-7">INDEX[7:0]</td><td id="20-8">As</td><td id="20-9">P</td></tr>
</table>
0x53 (read)
<table id="20-a">
<tr><td id="20-b">S</td><td id="20-c">ADDRESS[7:0]</td><td id="20-d">As</td><td id="20-e">DATA[7:0]</td><td id="20-f">Am</td><td id="20-g">DATA[7:0]</td><td id="20-h">Am</td></tr>
</table>
<table id="20-i">
<tr><td id="20-j">DATA[7:0]</td><td id="20-k">Am</td><td id="20-l">DATA[7:0]</td><td id="20-m">Am</td><td id="20-n">DATA[7:0]</td><td id="20-o">Am</td><td id="20-p">P</td></tr>
</table>

<a id='f3ec4514-5b61-4ab0-9981-f846fb9b65f0'></a>

## 4.1 I2C interface - timing characteristics

Timing characteristics are shown in Table 10. Please refer to Figure 17 for an explanation of the parameters used.

<a id='688c7242-8185-4ce6-ad81-ab43103ce82c'></a>

Table 10. I²C interface - timing characteristics for Fast mode (400 kHz)
<table id="20-q">
<tr><td id="20-r">Symbol</td><td id="20-s">Parameter</td><td id="20-t">Min.</td><td id="20-u">Typ.</td><td id="20-v">Max.</td><td id="20-w">Unit</td></tr>
<tr><td id="20-x">F12C</td><td id="20-y">Operating frequency</td><td id="20-z">0</td><td id="20-A"></td><td id="20-B">400</td><td id="20-C">kHz</td></tr>
<tr><td id="20-D">tLOW</td><td id="20-E">Clock pulse width low</td><td id="20-F">1.3</td><td id="20-G"></td><td id="20-H"></td><td id="20-I" rowspan="2">μs</td></tr>
<tr><td id="20-J">tHIGH</td><td id="20-K">Clock pulse width high</td><td id="20-L">0.6</td><td id="20-M"></td><td id="20-N"></td></tr>
<tr><td id="20-O">tSP</td><td id="20-P">Pulse width of spikes which are suppressed by the input filter</td><td id="20-Q"></td><td id="20-R"></td><td id="20-S">50</td><td id="20-T">ns</td></tr>
<tr><td id="20-U">tBUF</td><td id="20-V">Bus free time between transmissions</td><td id="20-W">1.3</td><td id="20-X"></td><td id="20-Y"></td><td id="20-Z">μs</td></tr>
<tr><td id="20-10">tHD.STA</td><td id="20-11">Start hold time</td><td id="20-12">0.26</td><td id="20-13"></td><td id="20-14"></td><td id="20-15" rowspan="3">μs</td></tr>
<tr><td id="20-16">tSU.STA</td><td id="20-17">Start set-up time</td><td id="20-18">0.26</td><td id="20-19"></td><td id="20-1a"></td></tr>
<tr><td id="20-1b">tHD.DAT</td><td id="20-1c">Data in hold time</td><td id="20-1d">0</td><td id="20-1e"></td><td id="20-1f">0.9</td></tr>
<tr><td id="20-1g">tSU.DAT</td><td id="20-1h">Data in set-up time</td><td id="20-1i">50</td><td id="20-1j"></td><td id="20-1k"></td><td id="20-1l" rowspan="3">ns</td></tr>
<tr><td id="20-1m">tr R</td><td id="20-1n">SCL/SDA rise time</td><td id="20-1o"></td><td id="20-1p"></td><td id="20-1q">300</td></tr>
<tr><td id="20-1r">tF</td><td id="20-1s">SCL/SDA fall time</td><td id="20-1t"></td><td id="20-1u"></td><td id="20-1v">300</td></tr>
<tr><td id="20-1w">tsu.STO</td><td id="20-1x">Stop set-up time</td><td id="20-1y">0.6</td><td id="20-1z"></td><td id="20-1A"></td><td id="20-1B">μs</td></tr>
<tr><td id="20-1C">Ci/o</td><td id="20-1D">Input/output capacitance (SDA)</td><td id="20-1E"></td><td id="20-1F"></td><td id="20-1G">10</td><td id="20-1H" rowspan="3">pF</td></tr>
<tr><td id="20-1I">Cin</td><td id="20-1J">Input capacitance (SCL)</td><td id="20-1K"></td><td id="20-1L"></td><td id="20-1M">4</td></tr>
<tr><td id="20-1N">CḶ</td><td id="20-1O">Load capacitance</td><td id="20-1P">–</td><td id="20-1Q">125</td><td id="20-1R">400</td></tr>
</table>

<a id='31b9fd54-4e78-4eff-8577-104fb62a68ae'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold, blue font with a horizontal line beneath it.::>

<a id='c975390b-de4f-422a-94e2-12e2d40ce84e'></a>

DocID031281 Rev 3

<a id='25691e6a-1c8a-4219-9c97-7defdf695892'></a>

21/35