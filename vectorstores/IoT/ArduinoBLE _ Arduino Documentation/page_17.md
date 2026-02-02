<a id='93e10077-1587-43df-9673-ee3c4bec3896'></a>

12/4/25, 2:49 PM

<a id='8678b430-64a0-42a0-b034-04f89a735907'></a>

ArduinoBLE | Arduino Documentation

<a id='62e41610-e1c5-4a94-a67b-4b99ab6b7710'></a>

ARDUINODOCS

<a id='663b2449-1d3a-4ce2-aa58-60e8791807ba'></a>

```c
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energ");
4 
5   while (1);
6 }
7 
8 Serial.println("BLE Central scan");
9 
10 // start scanning for peripheral
11 BLE.scan();
12 
13 BLE.stopScan();
```

<a id='bd5d867e-0372-4a7b-87f0-4600a9569056'></a>

v BLE.available()
Query for a discovered Bluetooth® Low Energy device that was
found during scanning.

<a id='6d4afbc9-9ee7-4679-95ca-28cc59201b0f'></a>

## Syntax

```
1 BLE.available()
```

<a id='eb17ef9a-ee4c-4b78-a312-2cc16ebdbfdf'></a>

Parameters

Nothing

<a id='f6f849d0-c765-45be-9cae-62a45d3840a2'></a>

## Returns

**BLEDevice** representing the discovered device.

<a id='99bc4565-fbe5-44d6-8d5a-9d77ef34e730'></a>

Example

____________________________________________________________________________________________________

<a id='4d85c41a-d482-40db-a023-b40aa70456ec'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='992b8607-6615-406b-8dc8-d0680fb58264'></a>

25/26