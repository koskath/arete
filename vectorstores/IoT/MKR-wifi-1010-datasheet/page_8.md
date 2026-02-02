<a id='1ce2326c-dd2f-491b-b768-8bf193c694f7'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='4757d89d-78f0-40ac-91d3-7c89b6391e01'></a>

Arduino® MKR WiFi 1010

<a id='9149d2d0-8316-4204-9fa2-d3c58a2a95e6'></a>

3.2 Wi-Fi® Module

3.3 Wi-Fi®/Bluetooth® Communication Module

<a id='a2ae7a3e-c4a7-4765-86ab-ee8772c66d22'></a>

Nina W102 is based on ESP32 and is delivered with a pre-certified software stack from Arduino. Source code for the firmware is available [1].

<a id='fbea2c84-17f7-4ccf-a397-dced14b42cc6'></a>

NOTE: Reprogramming the wireless module's firmware with a custom one will invalidate compliance with radio standards as certified by Arduino, hence this is not recommended unless the application is used in private laboratories far from other electronic equipment and people. Usage of custom firmware on radio modules is the sole responsibility of the user.

<a id='80aeecab-efd2-4197-96e2-7137bacfcdc7'></a>

3.4 Crypto Chips

The crypto chip in Arduino IoT boards is what makes the difference with other less secure boards as it provides a secure way to store secrets such as certificates and it also allows accelerating secure protocols while never exposing secrets in plain text.

<a id='426631a3-b699-4aa5-a423-f31536a2f924'></a>

3.5 Power Tree <::flowchart:Inputs: - V USB (MOSFET) - VIN (DIODE) Both inputs connect to V CHRG. From V CHRG, power flows to 3V8 (BQ24195L). From 3V8, power flows to 3V3 (LDO, 600mA). From 3V3, power splits to: - SAMD21G18 (30mA) - NINA W102 (320mA) - ECC508 (16mA) - User application (600mA) Legend: - Component: (represented by a white rectangle) - Power Rail: (represented by a red outlined rectangle) - Power I/O: (represented by a grey circle) - Max Current: (represented by a red circle) - Conversion Type: (represented by a teal circle): flowchart::> MKR WiFi 1010 Power Tree

<a id='bb2f6a87-362e-46bb-807c-8b76b762d68f'></a>

8 / 16

<a id='fdd1d170-89e5-4cff-96b3-c2a5973ef091'></a>

Arduino® MKR WiFi 1010

<a id='f48c5407-c760-4896-bfbf-9adde4a7dbef'></a>

Modified: 05/11/2025