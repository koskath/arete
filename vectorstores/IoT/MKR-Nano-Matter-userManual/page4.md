<a id='58695841-038a-4b49-b0ba-f4a87c718bbc'></a>

ARDUINODOCS

<a id='01380347-b5dc-4203-ba3f-47e4355ae715'></a>

<::An image of an Arduino Nano Matter board. The board is blue with various electronic components, including integrated circuits, resistors, and capacitors. It has pin headers labeled D12, D11, D10, D9, D8, D7, D6, D5, D4, D3, D2, RST, RX0, TX1 along the top edge, and D13, 3.3V AREF, A0, A1, A2, A3, A4, A5, A6, A7, 5V, NC, VIN along the bottom edge. A USB-C port is visible on the left side. Logos for 'NANO MATTER', 'ARDUINO', and 'SILICON LABS' are printed on the board. Three wires are connected to the bottom right pins: a red wire to '+5V', a black wire to 'GND', and another red wire to 'VIN' which is labeled '6-21V'.
: figure::>
Nano Matter externally powered

<a id='8e0a64f5-e1a9-451d-94b1-ae7d0ec53072'></a>

<::logo: Arduino
ARDUINO
Blue and white circular logo with a stylized infinity symbol.::>

<a id='62ee58da-30be-470a-b77d-6edd5a3004fd'></a>

For low-power consumption applications, the following hacks are recommended:

* Cut the power status LED jumper off to save energy.
* Power the board with an external **3.3 V power supply** connected to **3.3V** pin. This will not power the *USB bridge IC*, so more energy will be saved.

<a id='1c3213c8-dbd5-4a96-9364-fc54133817c2'></a>

<::diagram: Two Arduino Nano Matter boards are shown, one above the other, against a light blue background. The top board is viewed from the top, showing various components, integrated circuits, and pin headers. A black line points to a pin labeled "GND" on the top-left side of the board. A red line points to a pin labeled "+3V3" on the top-right side of the board. The bottom board is also viewed from the top, similar to the top board but with a different orientation of some labels. A line points from the board to a circular inset graphic showing a close-up of a small solder pad area with a cut line between two pads, labeled "LED JUMPER CUT". The bottom of the image has the caption: "Image showing the LED jumper and external 3.3 V power".::>

<a id='0e5024a5-2cd5-4efb-a2c4-448503b5916e'></a>

To power the board through the VIN pin you need to close the jumper pads with solder.
The maximum voltage supported is +5 VDC.

<a id='e2d42e01-9523-4129-83b4-b2716b041a33'></a>

# Install Board Core and Libraries
The **Silicon Labs** core contains the libraries and examples you need to work with the board's components, such as its Matter, Bluetooth® Low Energy, and I/Os. To install the `Nano Matter` core, navigate to **Tools > Board > Boards Manager** or click the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for `Nano Matter` and install the latest `Silicon Labs` core version.

<a id='baeff8ab-ba0b-4d4c-8ae3-0862fa15f207'></a>

<::screenshot
: The image displays a screenshot of the Arduino IDE (Integrated Development Environment) version 2.3.3, titled "sketch_nov22a | Arduino IDE 2.3.3".

The IDE window shows a menu bar at the top with options: "File", "Edit", "Sketch", "Tools", and "Help". Below the menu bar is a toolbar with icons for common actions (e.g., Verify, Upload) and a dropdown selector currently showing "Arduino Nano Matter".

The left sidebar of the IDE is open to the "Boards Manager" tab. Inside the Boards Manager, there's a search bar with "Nano Matter" typed in, and a "Type: All" dropdown.

The main content area on the right shows a code editor for "sketch_nov22a.ino" with basic C++ structure: "void setup() { // put your setup code here, to run once: }" and "void loop() { // put your main code here, to rus repeatedly: }".

Overlaying the Boards Manager section is a detailed card for "Silicon Labs by Silicon Labs". This card indicates that "2.1.0 installed" is the current version. It also lists "Boards included in this package:", specifically mentioning "Ezurio Lyra 24P 20dBm Dev Kit", "Arduino Nano Matter", "SparkFun...", and a "More info" link. At the bottom of the card, there's a version dropdown showing "2.1.0" and a "REMOVE" button.
::>
Installing the Silicon Labs core in the Arduino IDE

<a id='ec317f9c-793c-44ff-bc55-cfbc9840aff2'></a>

Hello World Example