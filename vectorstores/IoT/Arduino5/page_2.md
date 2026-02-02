<a id='8d75550c-22cc-4d22-85d8-3e9d2c0b2b58'></a>

12/4/25, 2:51 PM

<a id='f6b927c5-85c4-4690-8cc3-a4d1857ebba9'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='bc2a2b91-70e9-4460-a83a-5cc66a1a72ac'></a>

ARDUINODOCS

<a id='4a484926-ada1-4279-9c85-40722cb9db30'></a>

Arduino IDE (online or offline).
Arduino_MKRENV library installed.
MKR ENV Shield (link to store)
Arduino MKR family board (link to
store)

<a id='717f2559-4864-4028-a96f-ab6f71d333d1'></a>

# The Different Sensors on the Shield

Before we test out the MKR ENV Shield, let's take a look at the different sensors that come with it. In total, there are three sensors: the LPS22HB (atmospheric pressure), HTS221 (temperature & humidity) and TEMT6000 (light intensity).

<a id='b5c6d2c0-6c2b-439f-b607-997b13d98f5f'></a>

HTS221 Temperature & Humidity
Sensor

<a id='89d494bf-1138-4cdf-9839-3dd9acdd3aad'></a>

<::An image showing a blue circuit board (possibly an Arduino-compatible board) with a small, rectangular component highlighted in blue. A dark grey label box with white text "HTS221" is positioned above the highlighted component, indicating it as the HTS221 sensor.
: figure::>
The HTS221 sensor.

<a id='906aaa48-671c-4699-8be4-5fc15ab9c6d9'></a>

This sensor's range and accuracy make it
suitable for many interesting experimental
settings. There are two different functions
that we can call upon:

<a id='bdc01f26-b9c5-4b7a-b969-ae8c68cbcca5'></a>

`readTemperature()`
and
`readHumidity()`
. The return values are in
**Celsius**
and relative humidity, but we can also use the
command
`readTemperature(FAHRENHEIT)`
if we want to get our values in
**Fahrenheit**

<a id='fe3d9fe2-e7f0-440e-a560-9f871321655f'></a>

The temperature range goes between
-40 and +120 (C) and the accuracy is 
0.5 C in the range of 15 to +40 C.
The humidity range goes between 
3.5% rH (relative humidity), at 20 (C) to
+80% rH. The rH sensitivity is 0.004%
rH.

<a id='a5a7f638-969b-4999-97c8-da91ed9d4413'></a>

You can find more information about this file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='cffeef90-c353-43ba-aca2-d7a073e67b31'></a>

2/8