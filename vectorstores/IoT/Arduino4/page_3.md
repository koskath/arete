<a id='e3235c99-92a5-4269-b33c-8828e1d07ea6'></a>

12/4/25, 2:51 PM

<a id='f60f1a9b-2772-4e2e-8cf3-fe74b58d3647'></a>

Arduino_MKRENV | Arduino Documentation

<a id='6d66a4d0-0dac-451c-85a9-404119f4a738'></a>

ARDUINODOCS

<a id='e23c57ea-5ef5-48a2-8acd-18cdb4cc8646'></a>

## Returns
None.

## Example
```
1 ENV.end();
```

## See also
- begin()
- readTemperature()
- readHumidity()
- readPressure()
- readIlluminance()
- readUVA()
- readUVB()
- readUVIndex()

<a id='69eb483c-859f-4bc5-b5ee-3d2264f3e773'></a>

v readTemperature()
Read the temperature sensor's value. If no unit is specified as parameter, the value will be expressed in Celsius.

<a id='8f2d5a97-a56c-4a43-96d4-598bf16a6a68'></a>

## Syntax

```
1 ENV.readTemperature(unit)
```

<a id='25775d53-be17-45a5-9a49-07c06fa36c07'></a>

## Parameters

*unit*: FAHRENHEIT to get the temperature in Fahrenheit and CELSIUS to get the temperature in Celsius (default).

<a id='d13cf056-70f8-4276-8527-ec6805171fcd'></a>

## Returns

The sensor's temperature value as float in the specified unit.

<a id='b15dc297-39d3-43db-afc3-8adb1a631c99'></a>

Example

<a id='2ed9ca43-f59c-418b-9cb6-674cbd2dcc07'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='9899b577-2615-453b-8a52-faf190bc51b3'></a>

3/10