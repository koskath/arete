<a id='3f4e545a-61b3-4158-a29b-ba6284391851'></a>

12/4/25, 2:50 PM

<a id='2d5422a2-5acc-4a46-a188-98164fc3d4f2'></a>

ArduinoBLE | Arduino Documentation

<a id='b0fa45eb-c136-4b46-8af8-9882dec415d1'></a>

ARDUINODOCS

<a id='bc4b2f51-ba9f-4f57-8203-ceb2f019c6da'></a>

```c
1 // Bluetooth® Low Energy LED Switch Characteristic
2 BLEByteCharacteristic switchCharacteristic("19B16
3
4
5 byte properties = switchCharacteristic.properties;
6
7 if (properties & BLERead) {
8   // characteristic is readable ...
9 }
10
11 if (properties & (BLEWrite | BLEWriteWithoutResp)) {
12   // characteristic is writable ...
13 }
```

<a id='2473d987-06f9-4ef8-9623-3be1185729c1'></a>

bleCharacteristic.valueSize()

> Query the maximum value size of the specified BLECharacteristic.

<a id='d58a119f-0a4d-4727-86cc-d1f5e612aece'></a>

## Syntax

```
1 bleCharacteristic.valueSize()
```

<a id='e059208e-184b-4a32-a892-60a3d4405562'></a>

**Parameters**

None

<a id='55959da7-dd78-46a4-a972-996b81bed2dd'></a>

## Returns
The **maximum value** size of the characteristic (in bytes)

<a id='9f64f50f-5f71-48b9-8c50-e8949a29b4d6'></a>

Example

```
1 // Bluetooth® Low Energy LED Switch Characteristic
2 BLEByteCharacteristic switchCharacteristic("19B106
3
4
5
6 Serial.print("value size = ");
7 Serial.println(switchCharacteristic.valueSize());
```

<a id='ad95b19b-3345-4f39-8282-5437df71c472'></a>

bleCharacteristic.value()
Query the current value of the specified BLECharacteristic.

<a id='c4654af1-fc4b-402b-b5bb-caf54a31da52'></a>

Syntax

<a id='7c9d992b-7f1e-49da-a7ad-a43d86ea5bd4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='7e425225-b8c2-4a86-84ab-2106152ea0c5'></a>

7/22