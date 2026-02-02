<a id='30b42970-56d7-496f-a790-353f633866db'></a>

12/4/25, 2:51 PM

<a id='a82064a0-a4de-4a82-8c5e-a5e3bececc28'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='daac1032-7562-4861-b8ad-b015f490d57a'></a>

ARDUINODOCS

<a id='058f9a28-2561-48a9-8a0c-bfba971d4957'></a>

<::An image of a circuit board (likely a development board or shield) with various electronic components. A label points to a specific component on the board, indicating "VEML6075 (OLDER VERSIONS)". The board has multiple rows of pin headers along its long edges, and a smaller header or connector on one short edge. There's also what appears to be an SD card slot on the left side. The overall color scheme is blue for the PCB and grey for the background.: figure::>
The VEML6075 sensor.

<a id='c80c9221-c17c-40b2-9f10-fa76e656a939'></a>

The older versions of the MKR ENV Shields also has a UV sensor that can detect UVA and UVB wavelengths. The sensors can be read through the

`readUVA()`

and

`readUVB()`

commands. We can also use

`readUVIndex()`
to calculate the UV index.

The UV sensor's range and accuracy makes is suitable for a lot of scientific experiments. The temperature range of operation goes from -40 °C to +85 °C.

You can find more information about this sensor by reading it's [datasheet](https://example.com/datasheet).

<a id='488a9ce3-c738-4e54-a8a2-84de87cdb21a'></a>

# Circuit

The circuit in this tutorial is very simple. Just
attach the MKR ENV Shield on top of a MKR
family board (shown below is the MKR WiFi
1010 board).

<a id='c07e40b1-fd9f-4a06-9ce7-1c6addad3782'></a>

<::logo: [MKR ENV Shield / MKR Family Board] MKR ENV SHIELD, MKR FAMILY BOARD. The logo features two circuit boards, one labeled "MKR ENV SHIELD" and the other "MKR FAMILY BOARD," with arrows indicating a connection or placement from the shield to the board.::>

<a id='0ddb8f13-3942-452f-adf0-16a25c314bb6'></a>

# Programming the Board

We will now get to the programming part of
this tutorial.

1. First, let's make sure we have the drivers
installed for the board we are using. If we are
using the Cloud Editor, we do not need to
install anything. If we are using an offline
editor. we need to install it manually. This

<a id='ba8bfa56-2c95-4c99-a4ea-2b8f1a08aa81'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='37fdee61-6591-4535-b947-0c168e99c55a'></a>

5/8