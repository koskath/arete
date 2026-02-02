<a id='b82ea5d9-9977-4338-9376-77af7dd53449'></a>

12/4/25, 2:51 PM

<a id='dbd58217-5870-4fb8-a417-194776925b02'></a>

ArduinoBLE | Arduino Documentation

<a id='58d70b27-05f6-4936-845b-8bb1fc9f3d00'></a>

ARDUINODOCS

<a id='efb0d9d0-2311-4584-9f30-c9627216f48e'></a>

Example

```c++
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4   while (1);
5 }
6
7 Serial.println("BLE Central scan");
8
9 // start scanning for peripheral
10 BLE.scan();
11
12
13 BLEDevice peripheral = BLE.available();
14
15 if (peripheral) {
16   // ...
17
18   Serial.println("Connecting ...");
19
20   if (peripheral.connect()) {
21     Serial.println("Connected");
22   } else {
23     Serial.println("Failed to connect!");
24     return;
25   }
26 }
27
28 // discover peripheral attributes
```

<a id='5a41cd48-5984-491e-8215-1267c1a589d8'></a>

v bleDevice.appearance()
Query the appearance (BLE characteristic UUID 0x2a01) of a
Bluetooth® Low Energy device.

## Syntax

```
1 bleDevice.appearance()
```

## Parameters
None

## Returns
**Appearance value** (as a number).

## Example
```
```

<a id='cbb55dde-6480-4889-a67d-ce058ce557ce'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='39c36137-7b8d-4530-83d8-4253b7c8dd59'></a>

12/24