<a id='1cc852a9-e6f0-4d1d-87ce-450771a0d58f'></a>

**Notice,** The `LowPower.sleep` function call can be uncommented, and the standard `sleep` function call commented out, to enable deep sleep on the Arduino MKRFOX1200, which is beneficial when operating on batteries. It is possible to avoid using the `Serial`, and the `SigFox.debug()` that is, they're just for debugging purposes. In sleep mode, the device requires a manual reset before flashing it again.

<a id='b5e8925f-3666-424c-8fd1-5b82f2968c3d'></a>

## SmartEverything
SmartEverything is an IoT device specially designed for rapid prototyping, as it has full Arduino compatibility, with multiple sensors ready to use, like MEMS Pressure Sensor, Proximity and Ambient Light Sensor, iNEMO 9-axis inertial module, humidity and temperature sensors, and even NFC NTAG, or a GPS/GNSS integrated antenna. If these features are quite interesting by themselves, this board also integrates a Bluetooth Low Energy (BLE) and, of course, a Sigfox Module (Telit LE51-868 S 868MHz module).

<a id='2c787369-176d-4303-9f27-a9fd9b46d144'></a>

<::An electronic circuit board, labeled "SMARTEVERYTHING NFC V2". Visible text on the board includes: "NXP", "PROJECT BY AMEL-TECH", "PRODUCT BY CIPIERRE", "AMEL-TECH", "CIPIERRE.IT.COM", "1998 IF". Another component on the board is labeled "Telit", "LES1-868", "CE0682", "SIN-GPA405004LJ", and "Made in China". The board features various electronic components, connectors, and pins.: figure::>

<a id='2822c239-ea8a-4005-8e80-dcec3aaa3288'></a>

With these awesome features, we can use the board for multiple purposes, like vehicle tracking with the GPS, building a micro meteorological station, registering vibrations and impacts with the accelerometers, or any other use case. For this example, we will register just the temperature and humidity. This way, we have created a simple code that will register temperature and humidity every 10 minutes.

<a id='4b469303-bcc7-42f2-9435-66357bd9690e'></a>

Initial Setup

<a id='15f88b26-52f4-4e12-b22b-948be76195e7'></a>

14