<a id='22ec92e6-4364-414c-9251-d7d3ff530b1f'></a>

12/4/25, 2:51 PM

<a id='9f8ed2ad-892b-4c23-bf7f-340a3d509df9'></a>

ArduinoBLE | Arduino Documentation

<a id='7989c7c4-4e87-4ab2-b053-c48c3fdb3395'></a>

ARDUINODOCS

<a id='1bee55ac-204d-42be-a142-6ad7d0fcd4e7'></a>

```
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
26
27   // discover peripheral attributes
28
```

<a id='08caafda-124c-4457-8c95-b82697c0b9a6'></a>

## bleDevice.hasLocalName()
Query if a discovered Bluetooth® Low Energy device is advertising a local name.

### Syntax
```
1 bleDevice.hasLocalName()
```

### Parameters
Nothing

### Returns
**true**, if the device is advertising a local name,
**false** otherwise.

### Example

<a id='2df3bd1c-4353-4763-b096-58c2986b5c1d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='ad808b4d-56f8-4984-be85-86522b79387b'></a>

18/24