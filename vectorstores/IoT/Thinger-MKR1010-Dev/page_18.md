<a id='f4d69b5d-4e0b-4cdf-8cd6-54f2cf51ab5a'></a>

<::An overhead, slightly angled view of a compact microcontroller board, likely an Arduino Nano RP2040 Connect. The board features a USB-C port on one end, a small white push button, and various surface-mount components. Prominently visible are two main chips: one with "RP2040" and "2140" markings, and another larger chip with the Arduino infinity logo (a horizontal figure-eight with a plus sign on the left and a minus sign on the right) on a metallic housing. Pin headers line both long edges of the board. A metal bracket with the number "2037" is visible near the Arduino chip.: figure::>

<a id='e1d01fce-17f3-4058-a561-28aaae0d20ee'></a>

Arduino Nano RP2040

<a id='5f5324de-d4b6-4220-9582-697979884688'></a>

The integration with Thinger.io requires downloading an additional library called "Arduino WiFININA" that allows communicating with the U-BLOX WiFi module.

<a id='e0891514-ec71-46d0-a6eb-4bad80c417e5'></a>

This example will allow connecting the Arduino Nano RP2040 device to the cloud platform in a few lines using the WiFi interface. The `arduino_secrets.h` file just needs to be modified with the relevant information.

<a id='02979c87-f40f-4aeb-98e4-2a0ba40d2d3e'></a>

18