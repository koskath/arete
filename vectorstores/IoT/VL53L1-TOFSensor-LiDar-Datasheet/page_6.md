<a id='28559f7d-5200-43fd-9475-a1a4c9a011ad'></a>

Product overview

<a id='9832844f-02cb-499d-a219-686e7cd1fe5f'></a>

VL53L1X

<a id='d8a04f64-8638-45de-a19b-095e7291adfd'></a>

## 1.4 Application schematic

*Figure 3* shows the application schematic of the VL53L1X.

<a id='d69952aa-03a7-42d1-b698-28da9011c3f2'></a>

Figure 3. VL53L1X schematic<::A schematic diagram illustrating the connections for the VL53L1X sensor. The central component is the VL53L1X integrated circuit. On the left side, a "HOST" block is connected to several pins of the VL53L1X: pin 5 (XSHUT), pin 7 (GPIO1), pin 9 (SDA), and pin 10 (SCL). These four pins are also connected to the IOVDD rail via individual pull-up resistors. On the right side of the VL53L1X, pin 1 (AVDDVCSEL) and pin 11 (AVDD) are connected to the AVDD rail. The AVDD rail is filtered by two capacitors in parallel: a 100nF capacitor and a 4.7µF capacitor, both connected to ground. A text note next to these capacitors states: "Capacitors as close as possible to VL53L1X". The VL53L1X has multiple ground pins: pin 3 (GND), pin 4 (GND2), pin 6 (GND3), and pin 12 (GND4), all connected to a common ground reference. Other pins on the VL53L1X include pin 2 (AVSSVCSEL) and pin 8 (DNC).: schematic::>

<a id='d38381e5-635d-409a-8303-706396963a6a'></a>

Note:
Capacitors on external supply AVDD should be placed as close as possible to the AVDDVCSEL and AVSSVCSEL module pins.

<a id='f25e7b63-bacc-4d71-9b82-acaeb6db1377'></a>

Note: External pull up resistor values can be found in IC-bus specification. Pull ups are typically
fitted only once per bus, near the host. For suggested values see Table 3.

<a id='5b965693-adf0-442d-917b-39159a48b19a'></a>

Note: XSHUT pin must always be driven to avoid leakage current. A pull up is needed if the host state is not known.

<a id='dc0338a7-370a-4750-99b8-1d79f0005e75'></a>

_XSHUT_ is needed to use HW standby mode (no I&#178;C communication).

<a id='01b68f50-ec7d-4082-8b81-6d9910e818f2'></a>

Note: XSHUT and GPIO1 pull up recommended values are 10 kOhms

<a id='48a23c90-04c6-4d9c-9c9b-1a1d8ffc76b4'></a>

Note:
GPIO1 to be left unconnected if not used
Table 3 show recommended values for the pull up and series resistors for an AVDD of 1.8 V
to 2.8 V in I2C Fast mode (up to 400 kHz).

<a id='6f5ec403-7802-4fb7-895e-480551d9403b'></a>

Table 3. Suggested pull up and series resistors for I²C Fast mode
<table id="5-1">
<tr><td id="5-2">IC load capacitance (C₁) (1)</td><td id="5-3">Pull up resistor (Ohms)</td></tr>
<tr><td id="5-4">C₁ ≤ 90 pF</td><td id="5-5">3.6 k</td></tr>
<tr><td id="5-6">90 pF &lt; C₁ ≤ 140 pF</td><td id="5-7">2.4 k</td></tr>
<tr><td id="5-8">140 pF &lt; C₁ ≤ 270 pF</td><td id="5-9">1.2 k</td></tr>
<tr><td id="5-a">270 pF &lt; C₁ ≤ 400 pF</td><td id="5-b">0.8 k</td></tr>
</table>
1. For each bus line, Cₗ is measured in the application PCB by the customer.

<a id='56ac7c2e-6f1e-4864-8c4b-d8568c860fe2'></a>

6/35

<a id='b0fbdf24-ba27-416d-9f63-00cda4a462e5'></a>

DocID031281 Rev 3
---

<a id='1d367fdb-a68a-442b-be76-63ae19938f72'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold blue font, with a line underneath.::>