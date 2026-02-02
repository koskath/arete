<a id='576131e2-32e2-4ed1-9272-b7542ddbaec5'></a>

12/4/25, 2:51 PM

<a id='3457b018-43dd-4656-865d-aa793d8327b4'></a>

ArduinoBLE | Arduino Documentation

<a id='c9616af9-9311-4a98-85fa-81a7ac0e0117'></a>

ARDUINODOCS

<a id='4503d0b7-c4c4-4b92-aeb5-b59842275556'></a>

```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4 
5   while (1);
6 }
7 
8 Serial.println("BLE Central scan");
9 
10 // start scanning for peripheral
11 BLE.scan();
12 
13 
14 BLEDevice peripheral = BLE.available();
15 
16 if (peripheral) {
17   // ...
18 
19   // print the local name, if present
20   if (peripheral.hasLocalName()) {
21     Serial.print("Local Name: ");
22     Serial.println(peripheral.localName());
23   }
24 }
25 // ...
26 }
```

<a id='51b0efde-edbf-44fa-90bd-55b47033f413'></a>

✓ bleDevice.hasAdvertisedServiceUuid()
Query if a discovered Bluetooth® Low Energy device is advertising
a service UUID.

<a id='e64b68a1-5ee4-4ed6-8637-c5a58a2fc49b'></a>

## Syntax

```
1 bleDevice.hasAdvertisedServiceUuid()
2 bleDevice.hasAdvertisedServiceUuid(index)
```

<a id='52d3faec-0603-40af-b69a-35cf1d9e717e'></a>

## Parameters

**index**: optional, defaults to 0, the index of the service UUID, if the device is advertising more than one.

<a id='650dbe09-c3fe-4911-b199-05e661643310'></a>

## Returns

**true**, if the device is advertising a service UUID,
**false** otherwise.

<a id='0de7bdc3-7ee2-4d00-a1ab-5a3f3df3e24b'></a>

Example

________________________________________________________________________________

<a id='89318beb-50d2-4b5c-a505-32a650381ea4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='96082551-12ea-4b38-87ba-9cd0de05cf02'></a>

19/24