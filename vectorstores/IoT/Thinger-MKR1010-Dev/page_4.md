<a id='eff8a26c-99e3-412e-a2e1-40841915dfad'></a>

The CC3000 chip from Texas Instruments was one of the first low-cost WiFi chips that revolutionized the IoT maker ecosystem. In contrast to the other available WiFi alternatives, like the WiFi shield, the CC3000 appeared at a low cost (about 10$) for its time. It is a powerful chip as it integrates the whole TCP/IP stack and many other protocols. Some vendors, like Adadruit, started to build modules and libraries for integrating this chip with the Arduino ecosystem. Thanks to the libraries provided by Adafruit is then possible to build a connected device with a few lines of code.

<a id='7d87a658-7521-495d-a818-eeb09c58e9eb'></a>

<::A close-up photograph of a black Adafruit CC3000 WiFi module, version 1.1, on a white background. The module is rectangular with rounded corners, populated with various electronic components. A prominent metallic shield in the center has text:
Model: CC3000MOD
FCC ID: Z64-CC3000EM
IC: 4511-CC3000EM
LTC: 13430 15
R 007-AB0057

Around the edges of the board are solder pads labeled with functions. On the left side, from top to bottom, are "Adafruit CC3000 WiFi", then a series of pads labeled: "GND", "Debug", "TXD", and "RXD". On the right side, from top to bottom, are pads labeled: "IRQ", "UBEN", "CS", "MOSI", "MISO", "CLK", "UTN", "GND", and "3V3". There is also a component labeled "39AY1YM HC4050M G4". A small flower-like logo is visible on the top right corner of the board. The module is titled: Texas Instruments CC3000 WiFi module.
: figure::>

<a id='1a1104cb-622c-4d9b-99f9-db212b6a3950'></a>

For this module is required to have installed the **Adafruit CC3000 Libraries**, as they are directly used by the Thinger client. Install it directly from the Arduino Library Manager by searching `cc3000`.

<a id='d6290d1a-874d-40fa-b1fe-67b40ee00b3f'></a>

4