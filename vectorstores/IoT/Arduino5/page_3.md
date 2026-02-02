<a id='3bbdc50f-6da1-4779-9b31-ac256a4246ec'></a>

12/4/25, 2:51 PM

<a id='3b13d1e4-23d1-4f9f-82fb-52fea7f62b74'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='e9adeaeb-30e5-4bf4-872c-9694d03e5a57'></a>

ARDUINODOCS

<a id='39735172-607b-4f9a-8d6e-14a69bb20a8b'></a>

LPS22HB Atmospheric Pressure
Sensor

<a id='4112b6ae-f4ac-4e01-bad5-1731dbe2cbce'></a>

<::An image shows a circuit board with a small, dark blue rectangular component labeled "LPS22HB" in a callout box. The circuit board has various pins and other components. Below the image, the caption reads: The LPS22HB sensor.
: figure::>

<a id='3221962b-c812-4161-9cad-ee2438ea91cf'></a>

The atmospheric pressure can be read using
the command

<a id='e85bd8f8-d26c-4306-97b9-efa0f8388bb1'></a>

`readPressure()`
, which can take either no parameters or one
of the following three, which will determine
the units in which pressure will be expressed:

<a id='ee310ea9-8e86-4c6d-a61c-24b829c0f37a'></a>

PSI - the sensor returns data in pounds
per square inch.

<a id='3f046e78-be17-455f-9125-ab676a4e092a'></a>

MILLIBAR - the sensor returns data in millibars. Millibars are exactly the same as hectopascal, a unit that is more commonly used by meteorologists for weather reports.

<a id='05bd680c-4fff-49cb-a92a-827c767890db'></a>

KILOPASCAL - the sensor returns data in kilopascals - this is the default option.

<a id='e0d82c13-1505-4055-9611-6f784d2d930e'></a>

Take a look at the table below. Here, we can
see that hectopascal and millibars are exactly
the same, and that PSI is entirely different, as
it follows the imperial unit system.

<a id='7aae439d-835a-4206-bf79-ced36e763f5c'></a>

<table id="2-1">
<tr><td id="2-2">Kilopascal (kPa)</td><td id="2-3">Hectopascal (hPa)</td><td id="2-4">Millibar</td><td id="2-5">PSI</td></tr>
<tr><td id="2-6">1</td><td id="2-7">10</td><td id="2-8">10</td><td id="2-9">0.145038</td></tr>
<tr><td id="2-a">10</td><td id="2-b">100</td><td id="2-c">100</td><td id="2-d">1.45038</td></tr>
<tr><td id="2-e">25</td><td id="2-f">250</td><td id="2-g">250</td><td id="2-h">3.62594</td></tr>
</table>

<a id='6830e9e9-bfa6-4b94-b2f7-986e8d0e5401'></a>

The barometric pressure sensor functions as a digital output barometer; it processes the data collected from the movement of a suspended silicon membrane. The change of pressure on the membrane affects a Wheatstone bridge, where piezo resistances are measured with an analog-to-digital converter and processed digitally.

<a id='1b330470-1518-4f1f-ad63-275d846fedc3'></a>

The sensor's range and accuracy make it suitable for a wide range of scientific experiments. The pressure range measures between 260 and 1260 hPa, with an accuracy

<a id='074ed96a-c3bb-4fcd-8a85-ae1da7a9dea3'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='0d9b2a61-2cf5-433a-85ee-671646925184'></a>

3/8