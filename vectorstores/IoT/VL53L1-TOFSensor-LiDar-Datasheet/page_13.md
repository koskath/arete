<a id='2da62e22-c6e9-4f4a-b684-8c410b4077a1'></a>

VL53L1X

<a id='09e41b65-ccd4-49d3-bc25-7592b0427eb1'></a>

Functional description

<a id='f7d26260-da55-4ac8-b021-37fafd9a11bf'></a>

## 2.7 Ranging sequences
The following figure shows the combination of the driver commands and the system states.

<a id='a4fbc659-7f66-4ba5-86e2-1b2dd4f0217f'></a>

Figure 9. Autonomous sequence

<::
Power Supply
XShut
GPIO1 (Interrupt)
Driver Command: Start Ranging, Get Rang.1, Clear Int., Get Rang.2, Stop Rang.
System State: SW Standby, Ranging Init, Ranging1, Inter. Measurement, Ranging2, Inter. Measurement, SW Standby
Timing Budget
Inter Measurement Period
: chart::>

<a id='4c6eebf7-0e9e-4d73-addf-3b61658f7f8b'></a>

Note: *Timing budget and inter measurement timings are the parameters set by the user, using a dedicated driver function.*

<a id='405df380-9caa-442f-bd81-6c4d23ac1a64'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='4d9188ce-e7fd-4294-af2d-1cded99dfcc8'></a>

DocID031281 Rev 3

<a id='a6efb9a3-69d2-4ce6-ba7d-650b2d2b6e37'></a>

13/35