<a id='8c8439f3-8a31-4c33-9859-da3e33408844'></a>

12/4/25, 2:51 PM

<a id='95e31dcf-635b-452d-8276-d2c31b7c1302'></a>

Arduino_MKRENV | Arduino Documentation

<a id='478b392b-36f8-4c6f-adb0-2eefa0b4a385'></a>

ARDUINODOCS

<a id='1a13148e-4214-4a1c-b4b0-98031b12f900'></a>

readPressure()
readIlluminance()
readUVA()
readUVB()
readUVIndex()

<a id='045b2379-625f-43eb-9bfc-19b73cf644b8'></a>

readPressure()

Read the pressure sensor's value. If no unit is specified, the value will be expressed in kilopascal.

<a id='5eed13a6-8868-443f-bf5c-7d96ca80e3f5'></a>

## Syntax

```
1 ENV.readPressure(unit)
```

<a id='4b23d3d9-2a7f-4e8d-990d-c5fd6af066e2'></a>

## Parameters

unit: PSI to get the pressure in pound
per square, MILLIBAR to get the
pressure in millibar and KILOPASCAL
to get the pressure in kilopascal
(default).

<a id='d12099b8-84cf-438c-af0e-963fefc90a5d'></a>

## Returns

The sensor's pressure value as float in the specified unit.

<a id='2f201705-2284-4d54-be68-2c5bbe58ddba'></a>

## Example

```
1 Serial.print("Pressure = ");
2 Serial.print(ENV.readPressure());
3 Serial.println(" kPa");
```

<a id='1e52de22-f561-4fce-8246-757c4c290b53'></a>

## See also

* begin()
* end()
* readTemperature()
* readHumidity()
* readIlluminance()
* readUVA()
* readUVB()
* readUVIndex()

<a id='7e329bb8-9ed3-4cfe-9088-0742ef1ae0a4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='401ec97d-9336-46cc-a875-0e83ea5ff910'></a>

5/10