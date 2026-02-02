<a id='7c438814-1e6c-4b8a-bb88-9193c095939f'></a>

12/4/25, 2:51 PM

<a id='cc8c46c0-8f8d-4197-bc18-547a94678cf0'></a>

ArduinoBLE | Arduino Documentation

<a id='1eb18bf4-c6ad-4569-9cc9-9fb5a559625d'></a>

ARDUINODOCS

<a id='974b5723-044d-478f-849b-616b91a88867'></a>



<a id='64ac3e74-88b6-4c00-afcd-9242fd124cbc'></a>

```c
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
12 BLEDevice peripheral = BLE.available();
13
14 if (peripheral) {
15   // ...
16
17   // print the advertised service UUIDs, if present
18   if (peripheral.hasAdvertisedServiceUuid()) {
19     Serial.print("Service UUIDs: ");
20     for (int i = 0; i < peripheral.advertisedServiceUuidCount(); i++) {
21       Serial.print(peripheral.advertisedServiceUuid(i));
22       Serial.print(" ");
23     }
24     Serial.println();
25   }
26 }
27
28 //
```

<a id='6cc67a68-cb9f-4488-a5e4-711bb800e492'></a>

✓ bleDevice.connect()
Connect to a Bluetooth® Low Energy device.

<a id='c2ff2891-8e0b-4213-95f0-45c2263f39bc'></a>

## Syntax

```
bleDevice.connect()
```

<a id='d14560d5-1ee4-4775-90b2-4eefe89487a3'></a>

**Parameters**

None

<a id='dcbad363-9726-4804-b177-e7ee752adb99'></a>

Returns

**true**, if the connection was successful,

**false** otherwise.

<a id='71a742aa-6153-4be5-bbb5-d131a1d9e570'></a>

Example

___

<a id='7e7533dc-7795-4010-b507-02460ed27822'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='2f0d600e-1cc1-498d-b6ba-648cd926e09a'></a>

23/24