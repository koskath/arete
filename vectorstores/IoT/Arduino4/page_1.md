<a id='3db16be6-573b-40ef-9eeb-d3131d095f0c'></a>

12/4/25, 2:51 PM

<a id='719b4997-9ad1-4a38-b8e9-4b30f47adcb5'></a>

Arduino_MKRENV | Arduino Documentation

<a id='581d201e-c56e-4a4b-9c90-b0f43e1809ea'></a>

ARDUINODOCS

Search on Docs /

<a id='28686ef3-b200-467b-b49c-e2781544bc58'></a>

← Go Back

Library

<a id='8da0d689-93e2-4e0b-aba6-9441d3374644'></a>

Recents viewed

<a id='1a86baa5-1520-46a2-9945-deea2bb36b5d'></a>

Arduino_MKRENV
Arduino_MKRGPS
Arduino_APDS9960
Arduino_MKRIoTCarrier

<a id='f3a24a65-3774-4446-be83-7633bd613610'></a>

Home / Programming / Library / Arduino_MKRENV ON THIS PAGE

<a id='0da40dc9-8a96-4f29-b892-f560a715f005'></a>

SENSORS

# Arduino_MKRENV

option ARDUINO: [x]
LGPL-2.1 V1.2.1 Arduino 11/08/2021

Arduino <info@arduino.cc>
http://github.com/arduino-lib...
info@arduino.cc

Allows you to read the temperature, humidity, pressure, light and UV sensors of your MKR ENV Shield.

<a id='0840cef2-7626-462b-b055-eb15b7df6372'></a>

GO TO REPOSITORY

<a id='24c3f1f5-377f-4535-b34e-e6750fb9b1d4'></a>

Usage/Examples Compatibility Releases

The Arduino MKR ENV library allows you to read the sensors on the MKR ENV Shield. It manages the different interfaces used by the sensors on the shield to give you an uniform and simple set of functions to read them. The library takes care of the calculations needed to produce values in the requested units. The values returned are signed floats.

<a id='4a125b84-841f-4ddb-90e0-16480c064b29'></a>

To use this library:

```
1 #include <Arduino_MKRENV.h>
```

<a id='734265e1-04e1-434f-b302-2229ebb1dfdd'></a>

The Arduino MKR ENV library takes care of the sensor initialization and sets its values as follows:

Absolute pressure range: 260 to 1260 hPa.
Humidity range: 0 to 100% relative humidity (rH).
Humidity accuracy: ± 3.5% rH, 20 to +80% rH.
Temperature range -40 to 120 °C.
Temperature accuracy: ± 0.5 °C from 15 to 40 °C.
Lux range: 10 to 100,000 lux.
UVA/UVB resolution: 16-bit; unit µW/cm2.
UVIndex: 1 to 11+.

<a id='efd43ef1-5ed0-4f22-9fed-9ceda1dbcf2b'></a>

Usage/Examples
Compatibility
Releases
Methods +

<a id='e4c2e082-967b-40d2-a85d-2e7b75228337'></a>

Methods

\/ begin()

<a id='4db7b758-f400-4c93-a3a3-944fabc0a095'></a>

Help

<a id='732a9586-4371-4842-b76f-076eaa857e0f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='27dd4145-3270-4ffb-858c-67f6ee54ae90'></a>

1/10