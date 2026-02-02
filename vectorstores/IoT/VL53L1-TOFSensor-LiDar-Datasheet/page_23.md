<a id='9943eb1a-75be-46ec-b5d7-e06bd9b141de'></a>

VL53L1X

<a id='f8e50ccb-b771-4cd1-92f0-7b9fa6e1088a'></a>

Electrical characteristics

<a id='8f829073-6120-44ed-9375-8cea9f99ee9f'></a>

5 Electrical characteristics

<a id='b24875a4-3985-426f-b2e5-7e6deabec671'></a>

5.1 Absolute maximum ratings

Table 13. Absolute maximum ratings

<table id="22-1">
<tr><td id="22-2">Parameter</td><td id="22-3">Min.</td><td id="22-4">Typ.</td><td id="22-5">Max.</td><td id="22-6">Unit</td></tr>
<tr><td id="22-7">AVDD</td><td id="22-8">-0.5</td><td id="22-9"></td><td id="22-a">3.6</td><td id="22-b" rowspan="2">V</td></tr>
<tr><td id="22-c">SCL, SDA, XSHUT and GPIO1</td><td id="22-d">-0.5</td><td id="22-e"></td><td id="22-f">3.6</td></tr>
</table>

<a id='b1022811-00a2-4515-a863-81f024ddbe1e'></a>

Note:
Stresses above those listed in Table 13 may cause permanent damage to the device. This is a stress rating only and functional operation of the device at these or any other conditions above those indicated in the operational sections of the specification is not implied. Exposure to absolute maximum rating conditions for extended periods may affect device reliability.

<a id='f64af1de-e9cf-44df-a6aa-a3be33dc299a'></a>

5.2 Recommended operating conditions
Table 14. Recommended operating conditions (1)
<table id="22-g">
<tr><td id="22-h" colspan="2">Parameter</td><td id="22-i">Min.</td><td id="22-j">Typ.</td><td id="22-k">Max.</td><td id="22-l">Unit</td></tr>
<tr><td id="22-m" colspan="2">Voltage (AVDD)</td><td id="22-n">2.6</td><td id="22-o">2.8</td><td id="22-p">3.5</td><td id="22-q" rowspan="3">V</td></tr>
<tr><td id="22-r" rowspan="2">IO (IOVDD) (2)</td><td id="22-s">Standard mode</td><td id="22-t">1.6</td><td id="22-u">1.8</td><td id="22-v">1.9</td></tr>
<tr><td id="22-w">2V8 mode (3)(4)</td><td id="22-x">2.6</td><td id="22-y">2.8</td><td id="22-z">3.5</td></tr>
<tr><td id="22-A" colspan="2">Ambient temperature (normal operating)</td><td id="22-B">-20</td><td id="22-C"></td><td id="22-D">85</td><td id="22-E">°C</td></tr>
</table>

<a id='6eaec633-8fe2-4c26-bddf-9e4d13dc31fa'></a>

1. There are no power supply sequencing requirements. The I/Os may be high, low, or floating when AVDD is applied. The I/Os are internally failsafe with no diode connecting them to AVDD
2. XSHUT should be high level only when AVDD is on.
3. SDA, SCL, XSHUT and GPIO1 high levels have to be equal to AVDD in 2V8 mode.
4. The default driver mode is 1V8.
2V8 mode is programmable using device settings loaded by the driver. For more details please refer to the VL53L1X API user manual (UM2356).

<a id='23c21412-83a1-4ddf-837f-677041d2a875'></a>

## 5.3 ESD
The VL53L1X is compliant with ESD values presented in *Table 15*

<a id='95e13942-df12-472a-b3ca-e9614d0d147a'></a>

Table 15. ESD performances
<table id="22-F">
<tr><td id="22-G">Parameter</td><td id="22-H">Specification</td><td id="22-I">Conditions</td></tr>
<tr><td id="22-J">Human body model</td><td id="22-K">JS-001-2012</td><td id="22-L">± 2 kV, 1500 Ohms, 100 pF</td></tr>
<tr><td id="22-M">Charged device model</td><td id="22-N">JESD22-C101</td><td id="22-O">± 500 V</td></tr>
</table>

<a id='c73f726d-a1eb-4057-bd95-8d60ec5fdc26'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, futuristic blue font with a horizontal line underneath.::>

<a id='9833d65a-59af-4f03-a9f8-a12e9919add0'></a>

DocID031281 Rev 3

<a id='83ef723e-e8f3-486e-aa51-e4d295b36fbc'></a>

23/35