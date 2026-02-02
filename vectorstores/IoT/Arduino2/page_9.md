<a id='ee78d540-f302-4809-b740-f2bfad974812'></a>

12/4/25, 2:51 PM

<a id='35488780-3223-4387-8697-bce5d296706a'></a>

ArduinoBLE | Arduino Documentation

<a id='3d3fed59-8292-48d5-b2a4-df01e9e6d42a'></a>

ARDUINODOCS

<a id='1ee83438-698c-40f0-8bdc-327feaa61bba'></a>

[Empty Field]

<a id='bc0d52c7-be34-4525-b0a1-4e628e8c542c'></a>

1 bleDevice.characteristic(index)
2 bleDevice.characteristic(uuid)
3 bleDevice.characteristic(uuid, index)

<a id='e46d822b-3b80-48e6-a818-b2b0ab87d7d7'></a>

## Parameters

**index**: index of characteristic
**uuid**: uuid (as a **String**)

<a id='012b28ef-ab8d-402a-9cf3-8d06edb0bb5f'></a>

## Returns

**BLECharacteristic** for provided parameters

<a id='88f1242f-1136-4c81-ad30-f262e82cb3d4'></a>

Example

```cpp
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
28   Serial.println("Discovering attributes ...");
29 }
```

<a id='5be29873-5283-4b21-b864-31e6a47e0ab0'></a>

### bleDevice.discoverAttributes()
Discover all of the attributes of Bluetooth® Low Energy device.

## Syntax

```
1 bleDevice.discoverAttributes()
```

<a id='f99c9b92-674a-410f-a4d2-33389400bd02'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='ffd44084-3f46-4a1f-9e93-00fa814133ed'></a>

9/24