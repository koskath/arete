<a id='7e4192d3-73b6-4b03-8b56-635cbc8a0e33'></a>

• Connect the **SDA** pin to the I2C data **SDA** pin on your Arduino. On an UNO &
'328 based Arduino, this is also known as **A4**, on a Mega it is also known as
digital **20** and on a Leonardo/Micro, digital **2**

<a id='730b6ad9-9c87-41f3-8f0f-611ef78b9e9e'></a>

The MMA8451 has a default I2C address of **0x1D** and can be changed to 0x1C by tying the **A** pin to GND

<a id='b0159450-72b0-4b5d-b523-282cfcbaa8a4'></a>

## Download Libraries
To begin reading sensor data, you will need to download the Adafruit_MMA8451 library and the Adafruit_Sensor library from the Arduino library manager.

<a id='67c78e06-298a-4a06-99dc-9e1f0b9d29a8'></a>

Open up the Arduino library manager: <::A screenshot of the Arduino IDE (version 1.8.4) titled "demo". The menu bar shows File, Edit, Sketch, Tools, and Help. The "Sketch" menu is open, displaying options such as "Verify/Compile", "Upload", "Upload Using Programmer", "Export compiled Binary", "Show Sketch Folder", "Include Library", and "Add File...". The "Include Library" option has a sub-menu open to its right, showing "Manage Libraries..." highlighted, followed by "Add .ZIP Library...", a header "Arduino libraries", and then a list of libraries including "ArduinoHttpClient", "ArduinoSound", "AudioZero", and "Bridge". This visual demonstrates the steps to access the library manager by selecting "Sketch" > "Include Library" > "Manage Libraries...".: figure::>

<a id='88487957-a3a7-40cc-ba3c-a775342a60e1'></a>

Search for the **Adafruit MMA8451** library and install it

<a id='022e90cd-309e-4718-be3c-0ce55cf530e5'></a>

Type All Topic All adafruit mma8451

Adafruit MMA8451 Library by Adafruit

Arduino library for the MMA8451 Accelerometer sensors in the Adafruit shop

More info

Version 1.... Install

<a id='063df122-38c7-4267-b4b0-75f8014b21fa'></a>

Search for the **Adafruit Sensor** library and install it

<a id='5ce1f4e6-3ea9-49fd-b0a0-3a5465f1c992'></a>

Library Manager

Type All
Topic All
Adafruit_Sensor

Adafruit Unified Sensor by Adafruit Version 1.0.2 INSTALLED
Required for all Adafruit Unified Sensor based libraries. A unified sensor abstraction layer used by many Adafruit sensor libraries.
More info

<a id='8178dae0-1aad-43f4-b106-fdc90cc786de'></a>

We also have a great tutorial on Arduino library installation at:
http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use (https://
adafru.it/aYM)

<a id='4882cae6-fe34-40df-afef-ad048d23b4f0'></a>

© Adafruit Industries

<a id='cfbfa48d-91d8-4552-bf69-b15e412252ed'></a>

Page 10 of 21