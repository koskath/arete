<a id='801cc123-80cd-4b08-9cf6-9ca0d6653d03'></a>

12/4/25, 2:49 PM

<a id='3f542e9d-4ebe-4235-ac7a-5209d4fa39a8'></a>

ArduinoBLE | Arduino Documentation

<a id='6b109459-dfca-4474-a05c-c61eb68bca4c'></a>

ARDUINODOCS

<a id='5489ac3d-7713-4924-bc14-ac081c2f1f4c'></a>



<a id='9941bf8f-bbdc-44eb-846a-6d1097918ed3'></a>

## Syntax

```
1 BLE.setEventHandler(eventType, callback)
```

<a id='69682f7f-b5b5-4b12-b615-173a42fc5259'></a>

## Parameters

**eventType**: event type (BLEConnected, BLEDisconnected)
**callback**: function to call when event occurs

<a id='fdf47bbf-74bf-41d8-a347-f52aff4dad66'></a>

Returns

Nothing.

<a id='4b1f6ced-d8c9-4416-a8f9-a992b9dea1ad'></a>

Example

```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4 
5   while (1);
6 }
7 
8 // ...
9 
10 // assign event handlers for connected, disconnected
11 BLE.setEventHandler(BLEConnected, blePeripheralConnectHandler);
12 BLE.setEventHandler(BLEDisconnected, blePeripheralDisconnectHandler);
13 
14 
15 
16 void blePeripheralConnectHandler(BLEDevice central) {
17   // central connected event handler
18   Serial.print("Connected event, central: ");
19   Serial.println(central.address());
20 }
21 
22 void blePeripheralDisconnectHandler(BLEDevice central) {
23   // central disconnected event handler
24   Serial.print("Disconnected event, central: ");
25   Serial.println(central.address());
26 }
```

<a id='3a0a3094-1614-451d-a002-05f71d57f7b0'></a>

v BLE.connected()
Query if another Bluetooth® Low Energy device is connected

<a id='b0ef517b-4e55-422b-a917-662229558701'></a>

Syntax

<a id='49725903-be6a-40c0-b77f-9104ef7d53cb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='3a12b44b-af76-40ab-a1a4-52ea2f103ed2'></a>

7/26