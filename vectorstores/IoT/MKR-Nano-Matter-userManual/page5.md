<a id='a97af37b-d2f9-4dfb-a9b4-46a3fe33c1f9'></a>

ARDUINODOCS

<a id='f8a42939-91d5-4f23-ae2e-906977fc17b7'></a>

is correctly connected to the Arduino IDE and that the Silicon Labs core and the board
itself are working as expected.

<a id='28bf2dc6-a3b5-4458-901d-783704e54b07'></a>

Copy and paste the code below into a new sketch in the Arduino IDE.

<a id='62e545c4-4f00-4163-b046-12b7cadaa741'></a>

```c
1 // the setup function runs once when you press reset or power the
2 void setup() {
3   // initialize digital pin LED_BUILTIN as an output.
4   pinMode(LED_BUILTIN, OUTPUT);
5 }
6 
7 // the loop function runs over and over again forever
8 void loop() {
9   digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is t
10   delay(1000);                      // wait for a second
11   digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making
12   delay(1000);                      // wait for a second
13 }
```

<a id='ca4745e1-9fb3-4618-8a2c-ee3b5234f662'></a>

In the Nano Matter, the `LED_BUILTIN` macro represents the **red LED** of the built-in RGB LED of the board. Please refer to the image below.

<a id='40d6adb0-a32e-46cc-9cea-71755ded306d'></a>

To upload the code to the Nano Matter, click the **Verify** button to compile the sketch and check for errors; then click the **Upload** button to program the board with the sketch.

<a id='0a71045d-d6bf-43e7-afda-8e0fde88975e'></a>

<::screenshot: A screenshot of the Arduino IDE (version 2.3.2) displaying a "Blink" sketch. The title bar shows "Blink | Arduino IDE 2.3.2". Below the menu bar (File, Edit, Sketch, Tools, Help), a toolbar is visible. The toolbar includes icons for Verify (a checkmark), Upload (an arrow pointing right), and a dropdown menu showing "Arduino Nano Matter" selected. An overlay label points to the Verify and Upload buttons, stating "VERIFY AND UPLOAD BUTTONS".

The code editor pane displays the following C++ code with line numbers:
16 by Arturo Guadalupi
17 modified 8 Sep 2016
18 by Colby Newman
19
20 This example code is in the public domain.
21
22 https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink
23
24 // the setup function runs once when you press reset or power the board
25 void setup() {
26 // initialize digital pin LED_BUILTIN as an output.
27 pinMode(LED_BUILTIN, OUTPUT);
28 }
29
30 // the loop function runs over and over again forever
31 void loop() {
32 digitalWrite(LED_BUILTIN, HIGH); // turn the LED on (HIGH is the voltage level)
33 delay(1000); // wait for a second
34 digitalWrite(LED_BUILTIN, LOW); // turn the LED off by making the voltage LOW
35 delay(1000); // wait for a second
36 }
37
38

Caption: Uploading a sketch to the Nano Matter in the Arduino IDE::>

<a id='8d722fd0-048b-4d84-9718-d744ffeb6e21'></a>

You should now see the red LED of the built-in RGB LED turning on for one second, then off for one second, repeatedly.

<a id='42daf3dd-adef-4c76-ab9b-8ea27ef3902e'></a>

<::image: An Arduino Nano Matter development board, blue in color, with a USB-C cable plugged into its left side. The board features various electronic components, including integrated circuits, resistors, capacitors, and LEDs. Along the top edge, pin labels are visible: D12, D11, D10, D9, D8, D7, D6, D5, D4, D3, D2, RST, RX0, TX1. On the right side, "NANO MATTER" and "ARDUINO" logos are present, along with the Silicon Labs logo. Along the bottom edge, pin labels include: D13, 3.3V, AREF, A0, A1, A2, A3, A4, A5, A6, A7, 5V, NC, VIN. A green LED is illuminated near the USB port, indicating power or activity.:.::>

If everything works as expected, you are ready to continue searching and experimenting with this mighty board.

<a id='8061c50f-04af-4dcd-860f-21ecc6fbdde0'></a>

<::Arduino Nano Matter development board with a USB-C port on the left. The board is blue with various electronic components, integrated circuits, and pin headers.::>
<::The top row of pin labels includes: D12, D11, D10, D9, D8, D7, D6, D5, D4, D3, D2, RST, RX0, TX1.::>
<::The bottom row of pin labels includes: D13, 3.3V, AREF, A0, A1, A2, A3, A4, A5, A6, A7, 5V, NC, VIN.::>
<::There are two RST buttons. Logos visible include "SILICON LABS", "NANO MATTER", and "ARDUINO". A green LED is illuminated near the D12 pin.::>

<a id='d52241c7-9356-4c6a-8880-c348184c893e'></a>

Matter

<a id='1819cc2e-66d2-4fc7-8e6a-7d08fdd7c236'></a>

Developing Matter-compatible IoT solutions has never been easier with the Arduino