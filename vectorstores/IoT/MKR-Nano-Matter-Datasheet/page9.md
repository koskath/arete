<a id='7f3ab31a-49d7-4a87-af54-c8fff7a11a1b'></a>

<::logo: Arduino
A teal-colored infinity symbol with a plus sign on the right side and a minus sign on the left side.::>

<a id='4dad1bdd-1302-4287-a467-0ad612527404'></a>

Arduino® Nano Matter

<a id='3687aeb7-a8ed-4003-aca9-91a6b2736866'></a>

## 4.3 Power Supply
The Nano Matter can be powered through one of the following interfaces:

*   **Onboard USB-C® port:** Provides a convenient way to power the board using standard USB-C® cables and adapters.
*   **VIN pad:** Applying 6 to 21 VDC to the VIN pin of the Nano-styled header connector.
*   **5V pad:** Applying +5 VDC to the 5V pin of the Nano-styled header connector.

<a id='35ba74e5-cf77-4749-8fc3-2411bfa451db'></a>

A detailed figure below illustrates the power options available on the Nano Matter and the main system power architecture.

<a id='353d64c9-bf9e-4600-acd8-a63a776a8133'></a>

<::Power Tree Diagram
: flowchart::>
Nano Castellated Pins (JP1)
- 3.3V INPUT/OUTPUT
- VIN INPUT
- 5V INPUT/OUTPUT

USB-C® Connector (J1)
- VUSB +5V INPUT

VUSB from USB-C Connector (J1) and 5V from Nano Castellated Pins (JP1) connect to VUSB line.

VUSB line connects to D2 (diode).

Output of D2 connects to:
1. BUCK Regulator MP2322GQH (U3)
   - VIN MAX +21V
   - VOUT +3V3
2. LDO Regulator AP2112K-3.3TRG1 (U2)
   - VIN +5V
   - VOUT +3V3

VIN from Nano Castellated Pins (JP1) also connects to VIN of BUCK Regulator (U3).

Output VOUT +3V3 from BUCK Regulator (U3) connects to Solder Jumper Normally Closed (SJ2).
- Information: Cut SJ2 to disable the 3V3 power rail.

The line after SJ2 is labeled +3V3. This +3V3 line connects to:
1. Microcontroller MGM240SD22VNA2R (U5)
2. LED RGB (DL1)
3. Reset Button (PB1)
4. Solder Jumper Normally Closed (SJ4)
   - Information: Cut SJ4 to disable the power LED and save energy.

3.3V from Nano Castellated Pins (JP1) also connects to Microcontroller (U5).

Output of SJ4 connects to Power LED (DL2).

Output VOUT +3V3 from LDO Regulator (U2) connects to USB Bridge ATSAM-D11-D14A-MUT (U1) via a line labeled +3V3_D11.

Legend:
- Red: +3V3
- Light Blue: +3V3_D11
- Yellow: +5V
- Dark Blue: VUSB
- Orange: Connector
- Gray: Internal Part

ARDUINO
Nano Matter
SKU code: ABX00112
Power Tree
Last update: 02 Dec, 2024

<a id='373452aa-181b-4bde-839e-0d91a0a7469b'></a>

**Low-Power Tip:** For power efficiency, safely cut the LED jumper and connect an external +3.3 VDC power supply to the board's 3V3 pin. This configuration does not power the board's USB bridge.

<a id='11740382-089e-4576-80d4-5be7f105e36b'></a>

Safety Note: Disconnect power before board modifications. Avoid short-circuiting. Refer to the full guide for more safety tips.

<a id='7333fb5c-19d2-4344-bece-f2cf3b6bd5ae'></a>

9 / 18

<a id='34bd3323-1972-47b2-ad1e-70cf236c0020'></a>

Arduino® Nano Matter

<a id='c9e76fa3-feed-4dad-b223-445adc8f8b6e'></a>

Modified: 29/01/2026