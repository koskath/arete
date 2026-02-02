<a id='22e52980-98fc-4429-a88c-45a8c655496f'></a>

12/4/25, 2:51 PM

<a id='efc9e4c0-f0da-40dc-8fb7-6cf6b78af6ed'></a>

ArduinoBLE | Arduino Documentation

<a id='2c2ec017-f66e-4863-bdc7-fbdf027d898b'></a>

ARDUINODOCS

<a id='cd8dc661-2275-41a2-841e-c733dfc091e5'></a>



<a id='13277a7c-986d-4d05-bce6-6d1f6f22a14e'></a>

```
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
19   // print the advertised service UUIDs, if present
20   if (peripheral.hasAdvertisedServiceUuid()) {
21     Serial.print("Service UUIDs: ");
22     for (int i = 0; i < peripheral.advertisedServiceUuidCount(); i++) {
23       Serial.print(peripheral.advertisedServiceUuid(i));
24       Serial.print(" ");
25     }
26     Serial.println();
27   }
28 }
29 //
```

<a id='d1d027c1-7514-4809-a8c5-de6180e5ab3c'></a>

✓ bleDevice.advertisedServiceUuidCount()
Query the number of advertised services a discovered Bluetooth® Low Energy device is advertising.

<a id='d3fcd8e9-604c-411a-aee1-ce0e784b0ff8'></a>

## Syntax

```
1 bleDevice.advertisedServiceUuidCount()
```

<a id='32871765-98f6-4380-8fb7-e3d599616068'></a>

Parameters

None

<a id='1a479121-a54b-4e19-b8da-29a10c2d4385'></a>

Returns
The number of **advertised services** a discovered Bluetooth®
Low Energy device is advertising.

<a id='93a852de-e285-4b92-96aa-03c550669fe4'></a>

Example

---

<a id='a70a2a49-82fc-4510-98b9-b27fe12602d8'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='c6bac505-9728-4699-98d8-4b754052502e'></a>

20/24