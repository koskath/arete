<a id='c06a15de-bdd9-4893-9e6a-13b9f028ced5'></a>

ARDUINODOCS

<a id='026b8cbb-913b-4d19-8b16-460d8f962a82'></a>

<::An image of an Arduino Nano microcontroller board. A label "RESET BUTTON" with an arrow points to the physical reset button on the board. The board's pin labels are visible around its perimeter: D12, D11, D10, D9, D8, D7, D6, D5, D4, D3, D2, RST, RX0, TX1 along the top edge, and D13, 3.3V, AREF, A0, A1, A2, A3, A4, A5, A6, A7, 5V, NC, VIN along the bottom edge. The board also features the "NANO MATTER" and "ARDUINO" logos.: figure::>

<a id='dbc29b9f-0c7b-47e0-bd69-1dcd9ca9cb0a'></a>

<::An image of an Arduino Nano Matter development board, viewed from above. The board is dark blue with various electronic components, pins, and labels. A white reset button is centrally located on the left side of the board and is highlighted with a white outline. 

Key labels and pins visible on the board include:
- Top edge (left to right): D12, D11, D10, D9, D8, D7, D6, D5, D4, D3, D2, RST, RX0, TX1
- Bottom edge (left to right): D13, 3.3V, AREF, A0, A1, A2, A3, A4, A5, A6, A7, 5V, NC, VIN
- Other visible text and logos: "SILICON LABS", "NANO MATTER", "ARDUINO" logo.
- A USB-C port is visible on the far left edge of the board.
: figure::>

<a id='10acf9e3-750a-48ee-b84b-acca59af31b6'></a>

Nano Matter Reset Button

<a id='9e3da51f-8543-4713-add0-bd0d89ee6a8c'></a>

You will find a **Manual pairing code** and a **QR code URL** as follows:

<a id='3fbfaa3a-cce3-4ff6-b2f0-54c19c519342'></a>

<::figure: The image displays two open computer windows side-by-side. On the left is an Arduino IDE window, titled "nano_matter_lightbulb | Arduino IDE 1.8.2". The code editor shows a C++ sketch named "nano_matter_lightbulb.ino" with comments explaining it's a Matter color lightbulb example for Arduino Nano Matter, allowing control of an onboard RGB LED. The code includes Matter.h and MatterLightbulb.h libraries and defines GPIO pins for red, green, and blue LEDs. Below the code, the serial monitor output indicates that the "Matter device is not commissioned" and provides instructions to commission it using a manual pairing code (000Y1072) or a QR code URL. On the right is a web browser window, titled "CHIP QR Code", displaying a QR code. The page instructs, "Please scan with your CHIPTool app." Below the QR code, it shows "Payload: MT:NFCJ:42C00KA0648G00" and states, "This QR code is unique for your device. You may print a copy of this for subsequent use." A button labeled "Print QR Code" is visible, and the footer reads, "This QR code is generated using qrcodes".::>
Commissioning credentials

<a id='e12f0c3a-3266-46e5-987d-e93447d7e305'></a>

Open the QR code URL on your browser to generate the QR code.

<a id='d7aaa90b-4b7c-4a1e-8bfc-7b991d5d48e3'></a>

## With Google Home™

To create your first IoT device with the Nano Matter and the Google Home ecosystem, you first need to have a Matter-compatible hub. The Google Home products that can work as a **Matter hub** through **Thread®** are listed below:

*   Nest Hub (2nd Gen)
*   Nest Hub Max
*   Nest Wifi Pro (Wi-Fi 6E)
*   Nest Wifi

<a id='bd7954ea-1bb3-4827-87c0-ad7b0b50b6ba'></a>

Other Google devices are compatible with Matter but not Thread®.

<a id='071dbaa2-8eef-4939-9c26-4be5218476b3'></a>

To commission your device, open the Google Home app, navigate to devices, click on
**add device** and select the **matter-enabled device** option:

<a id='9ac3d3d6-f8d3-4b00-acac-ee62f4d32756'></a>

<::Multi-panel figure showing the process of adding a device to Google Home. The panels display smartphone screens.

Panel 1: The first screen shows the 'Devices' tab of the Google Home app.
Top bar: 4:09, Wifi signal icon, Battery icon (90%).
Header: Devices, Settings icon, User icon.
Rooms and devices listed:
Cocina (Kitchen):
  Cocina: [ ] (square icon)
  Luz de la cocina: [ ] OFF (lightbulb icon)
Habitación (Room):
  Televisión: [ ] OFF (TV icon)
  Nest Mini: [ ] (speaker icon)
  Luz de la habitación: [ ] OFF (lightbulb icon)
  Aire: [ ] OFF (fan icon)
Lavadero (Laundry room):
  Área de lavado: [ ] OFF (washing machine icon)
  Lavadora: [ ] Stopped (washing machine icon)
Pasillo (Hallway):
  '+ Add' button.
Bottom navigation bar: Favorites (heart icon), Devices (house icon, selected), Automations (automation icon), Activity (clock icon), Settings (gear icon).

Arrow pointing right.

Panel 2: The second screen shows the 'Choose a device' menu.
Top bar: 4:09, Wifi signal icon, Battery icon (90%).
Header: Choose a device.
Options:
  Matter-enabled device (highlighted in yellow):
    Add devices with the Matter logo.
  Google Nest or partner device:
    Add Nest devices, Chromecast, Google Assistant-enabled devices, or partner devices labeled "Seamless Setup with the Google Home app".
  Works with Google Home:
    Link existing devices or services labeled "Works with Google Home".

Arrow pointing right.

Panel 3: The third screen shows the 'Scan Matter QR code' interface.
Top bar: 4:10, Wifi signal icon, Battery icon (90%).
Header: Scan Matter QR code.
Text: Make sure it's steady and well-lit.
Content area displays a representation of a smartphone screen showing a web page:
  URL: https://project-chip.github.io/connectedhomeip/qr.html
  Text: Please scan with your CHIPTool app.
  A large QR code is visible, with a small icon at the bottom right that appears to be for manual code entry.
Button: Set up without QR code.
: multi-panel figure::>