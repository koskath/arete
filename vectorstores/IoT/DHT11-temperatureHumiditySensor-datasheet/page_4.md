<a id='795f2c3a-0442-4a01-ac17-c59e3bf40e1e'></a>

<::logo: AOSONG
AOSONG
Aosong Electronics
Blue stylized text "AOSONG" with "Aosong Electronics" underneath, framed by two blue horizontal lines.::>

<a id='82732d93-6add-46fc-8088-5426d09487e3'></a>

Temp、Humidity & Dew point measurement experts

<a id='86ff7d23-9501-41b1-b611-14b4d88811cf'></a>

Supply current : Measure 0.3mA Standby 60µA
Sampling period : Secondary Greater than 2 seconds

<a id='a4bc253c-5b55-4cac-bef0-1110c13bb43e'></a>

### Pin Description
1. VDD supply 3.3 ~ 5.5V DC
2. DATA serial data, single-bus
3. NC NC
4. GND grounding, power negative

<a id='85fd2a73-eacf-412d-858d-e46452193289'></a>

6. Typical circuit
<::A circuit diagram showing a microcontroller, a power supply, a DHT11 sensor, and a 4-digit 7-segment display.

**Microcontroller Section:**
- The microcontroller's VCC pin is connected to a VCC line via a resistor.
- OSC1 and OSC2/CLK pins are connected to an external crystal oscillator circuit with two capacitors to ground.
- Pins P3.0, P2.0, and P2.3 are connected via individual resistors to the bases of three NPN transistors. The collectors of these transistors are connected to the common anodes of three digits of a 4-digit 7-segment display, and their emitters are connected to ground.
- Pins P1.0 through P1.7 are connected directly to the segment inputs (a-g, DP) of the 4-digit 7-segment display.

**DHT11 Sensor Section:**
- The DHT11 sensor has four pins: 1, 2, 3, 4.
- Pin 1 is connected to VCC.
- Pin 2 (labeled I/O) is connected to a VCC line via a pull-up resistor.
- Pin 3 is labeled NC (Not Connected).
- Pin 4 is connected to GND.

**Power Supply Section:**
- A 7805 voltage regulator is used.
- The VI (input voltage) pin is connected to a `V+` input, with a capacitor to ground.
- The GND pin is connected to ground.
- The VO (output voltage) pin is connected to VCC, with a capacitor to ground.
: circuit diagram::>

<a id='21671130-d289-48e9-b1ab-086628c9a9e6'></a>

Connecting the typical application circuit shown above the microprocessor and DHT11, DATA pull-up and microprocessor I/O port.
1. A typical application circuit recommended cable length shorter than 20 meters with a 5.1K pull-up resistor when greater than 20 meters when the pull-up resistor to reduce the actual situation.
2. When using a 3.3V voltage supply cable length must not be greater than 100cm. Otherwise it will lead to lack of line drop sensor supply, causing measurement bias.
3. Temperature and humidity values are read out every last measurement result, want to get real-time data, to be read twice in a row, but not recommended repeatedly read sensors, each sensor reading interval of more than 5 seconds to obtain accurate data.

<a id='b740dd62-ccaa-4cf8-9a5c-31fb379f78a9'></a>

## 7. Serial Communications Description (single-wire bidirectional)

© Single Bus Description

<a id='c4e032a3-49b8-4d81-bfcb-94f35dd49537'></a>

DHT11 device uses a simplified single-bus communication. Single bus that only one data line,
the data exchange system, are controlled by a single bus is complete. Device (master or slave)
through an open-drain or tri-state port is connected to the data line to allow the device to send data
when not able to release the bus, and let other devices use the bus; single bus usually requires an

<a id='c87585f3-3f93-494c-b220-2b8a330e6c02'></a>

Aosong Guangzhou Electronics Co., Ltd.

<a id='bd855eb8-9dad-491b-9613-4770f658105a'></a>

Order by phone : 4006 305378

<a id='1b5b0b35-a3cf-433f-bafd-5f9a1c1b2889'></a>

Enterprise QQ: 4006305378

<a id='4bceac2b-fbbb-4bba-a52f-cff64c6c5b25'></a>

www.aosong.com