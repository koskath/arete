<a id='22bfbe2c-bc33-456c-816e-28dc9792c86a'></a>

12/4/25, 2:50 PM

<a id='aadee55d-2319-4a4b-b38b-b75edb1c16eb'></a>

ArduinoBLE | Arduino Documentation

<a id='023fc917-d517-43c3-b8a8-b1826b6a7cd2'></a>

ARDUINODOCS

<a id='53e05cc5-48c2-4779-ad5d-42a40df0d44a'></a>



<a id='af79c391-3926-4d41-bd14-83387b9439fb'></a>

1 bleCharacteristic.value()

<a id='fbb5fb32-adee-42be-924b-b7eec55fbce3'></a>

Parameters

None

<a id='115cecd0-65db-4a56-bece-878b8fa0a0fe'></a>

## Returns

The **current value** of the characteristic, value type depends on the constructor used

<a id='8bf21a08-1bbb-498e-8258-bb4a25c019dc'></a>

Example

```
1 // Bluetooth® Low Energy LED Switch Characteristic
2 BLEByteCharacteristic switchCharacteristic("19B16
3 
4 
5 
6 if (switchCharacteristic.value()) { // any value
7   Serial.println("LED on");
8   digitalWrite(ledPin, HIGH); // will turn the
9 } else { // a 0 value
10   Serial.println(F("LED off"));
11   digitalWrite(ledPin, LOW); // will turn the
12 }
```

<a id='a567479c-ba37-4267-b534-f92673b44148'></a>

### bleCharacteristic.valueLength()
Query the current value size of the specified BLECharacteristic.

### Syntax

```
1 bleCharacteristic.valueLength()
```

<a id='029ccaf8-d329-40e9-aec7-b99d31399803'></a>

Parameters

None

<a id='7f51aefe-0626-4015-8547-75c51c1d3152'></a>

Returns

The **current value** size of the characteristic (in bytes)

<a id='c8ff9747-2979-450c-b766-d1388af5830c'></a>

Example

________________________________________________________________________________

<a id='c56f1e63-4f17-49d2-a16a-2c7c23918486'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='2cfdd82f-6310-4984-bf0e-0f93e920338d'></a>

8/22