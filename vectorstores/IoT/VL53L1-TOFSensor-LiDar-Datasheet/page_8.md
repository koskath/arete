<a id='7b3a65dd-a190-451d-96e2-dda81c190413'></a>

Functional description

<a id='f10a1b73-1eae-4e1f-9d25-ec73676cc4b1'></a>

VL53L1X

<a id='d8988ab7-9dc5-4256-8bd8-c86692348e42'></a>

## 2.2 System state machine description

Figure 5 shows the system state machine.

<a id='d119d6de-51bc-4452-ac3b-014cf56bb190'></a>

Figure 5. System state machine
<::
flowchart::>
Legend:
- Device States or action: Yellow rounded rectangle
- Host action: Blue rectangle

Flowchart starts with "Power Off" (Device State).

From "Power Off":
- An arrow points to "VDD lowered" (Host action).
- An arrow points to "VDD raised" (Host action).
- An arrow from "VDD lowered" points to "Power Off".
- An arrow from "VDD raised" points to "Power Off".

From "VDD lowered" (Host action):
- An arrow points to "HW Standby" (Device State).
- An arrow from "HW Standby" points to "VDD lowered".

From "VDD raised" (Host action):
- An arrow points to "HW Standby" (Device State).
- An arrow from "HW Standby" points to "VDD raised".

From "HW Standby" (Device State):
- An arrow points to "XSDN lowered" (Host action).
- An arrow points to "XSDN raised" (Host action).
- An arrow from "XSDN lowered" points to "HW Standby".
- An arrow from "XSDN raised" points to "HW Standby".

From "XSDN lowered" (Host action):
- An arrow points to "SW Standby" (Device State).
- An arrow from "SW Standby" points to "XSDN lowered".

From "XSDN raised" (Host action):
- An arrow points to "SW Standby" (Device State).
- An arrow from "SW Standby" points to "XSDN raised".

From "SW Standby" (Device State):
- An arrow points to "Start Measurement" (Host action).
- An arrow from "Stop Measurement" (Host action) points back to "SW Standby".

From "Start Measurement" (Host action):
- An arrow points to "Ranging" (Device State).

From "Ranging" (Device State):
- An arrow points to "Interrupt raised" (Device State).
- An arrow from "Inter meas. completed ?" (Decision) 'YES' path points back to "Ranging".

From "Interrupt raised" (Device State):
- An arrow points to "Get ranging data" (Host action).

From "Get ranging data" (Host action):
- An arrow points to "Clear interrupt" (Host action).

From "Clear interrupt" (Host action):
- An arrow points to "Stop ?" (Decision).

From "Stop ?" (Decision):
- If 'YES', an arrow points to "Stop Measurement" (Host action).
- If 'NO', an arrow points to "Inter meas. completed ?" (Decision).

From "Inter meas. completed ?" (Decision):
- If 'YES', an arrow points back to "Ranging" (Device State).
- If 'NO', an arrow points to "Wait for inter meas completed" (Device State).

From "Wait for inter meas completed" (Device State):
- An arrow points back to "Inter meas. completed ?" (Decision).
<::

<a id='38c68f07-7a21-4376-969d-49b3b0b10953'></a>

8/35

<a id='3130b303-b454-4715-b88c-b0dbbd566247'></a>

DocID031281 Rev 3

<a id='8bced8ab-e18f-419f-8f01-079b1b6ac8bf'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, modern font, with the "T" integrated into the "S", and a horizontal line beneath it, all in blue.::>