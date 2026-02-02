<a id='2b83a105-6deb-4703-b701-91faae70ec77'></a>

12/4/25, 2:51 PM

<a id='f1333506-4d95-46b1-a65a-82e9d75844c2'></a>

ArduinoBLE | Arduino Documentation

<a id='bdec0f0e-64dc-4653-8bff-356bc18dce53'></a>

ARDUINODOCS

<a id='c2f2f7ab-7998-4800-84b6-8b59079d9fae'></a>

Returns

**true**, if successful,
**false** on failure.

<a id='541f29bf-69dd-4b94-b94e-81b9ac7a08e5'></a>

Example

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Ene
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
28 // discover service attributes
```

<a id='91bf1456-f0b7-4402-b5df-c25182c4b19d'></a>

v bleDevice.deviceName()
Query the device name (BLE characteristic UUID 0x2a00) of a
Bluetooth® Low Energy device.

<a id='33eaee89-5703-45b0-b893-52d1dd4bef1d'></a>

## Syntax

```
1 bleDevice.deviceName()
```

<a id='fc25890c-e2ad-421d-8446-8b33ee7623c8'></a>

**Parameters**

None

<a id='369417b7-8edd-4d85-86d2-a0565b0ee340'></a>

Returns

<a id='9e4e7b8b-916f-4a87-ac33-1a2ce7098316'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='5fd13aa1-149f-4865-bd53-2f0b295fd260'></a>

11/24