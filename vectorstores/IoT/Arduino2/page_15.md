<a id='b8718940-dad8-4c72-9c5e-24a246268a12'></a>

12/4/25, 2:51 PM

<a id='65d1275f-3f85-470a-864b-55c9de022583'></a>

ArduinoBLE | Arduino Documentation

<a id='bd22b26a-d0e0-4228-95f9-b4aad543a328'></a>

ARDUINODOCS

<a id='964ee5c7-ed26-4fcb-9bbf-cb746f6517ee'></a>

```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Ene");
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

<a id='2a42d94e-33a5-4775-8266-0390811b78f9'></a>

bleDevice.service()
Get a BLEService representing a Bluetooth® Low Energy service the device provides.

### Syntax

```
1 bleDevice.service(index)
2 bleDevice.service(uuid)
3 bleDevice.service(uuid, index)
```

### Parameters

index: index of service
uuid: uuid (as a String)

### Returns

BLEService for provided parameters

### Example

<a id='dacff8c7-426d-4ebd-a402-fb58eacab368'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='55318519-0bf4-47d3-b488-70e1dc318f74'></a>

15/24