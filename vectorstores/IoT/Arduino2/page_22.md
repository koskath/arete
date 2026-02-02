<a id='0de03a74-6ca2-4796-bf51-c97008b69091'></a>

12/4/25, 2:51 PM

<a id='9bf84ee6-5a51-4c17-8251-88b0e18ea5e4'></a>

ArduinoBLE | Arduino Documentation

<a id='bff8beb9-c191-4271-8f64-8d81dfbd4cb6'></a>

ARDUINODOCS

<a id='2a673a4b-b08e-4862-a3db-b73e08363157'></a>

```c
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Ener{");
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
18   // print the local name, if present
19   if (peripheral.hasLocalName()) {
20     Serial.print("Local Name: ");
21     Serial.println(peripheral.localName());
22   }
23 }
24 // ...
25 
26 
```

<a id='62ec5d6b-8272-46ef-adeb-2cc8761842ef'></a>

✓ bleDevice.advertisedServiceUuid()
Query an advertised service UUID discovered Bluetooth® Low
Energy device is advertising.

<a id='89e7df42-cbb4-48d5-b1bb-43d1f911f1bf'></a>

## Syntax

```
1 bleDevice.advertisedServiceUuid()
2 bleDevice.advertisedServiceUuid(index)
```

<a id='bfdcf560-0366-4bc8-828d-689fb10fa06c'></a>

## Parameters

**index**: optional, defaults to 0, the index of the **service UUID**, if the device is advertising more than one.

<a id='2b1044a8-3229-4d76-833a-6830080ebd9e'></a>

# Returns

Advertised service **UUID** (as a String).

<a id='6cedcaaa-84f1-490f-b499-dd10f8dca399'></a>

Example

___

<a id='17d20161-7b3d-4a4c-af3c-cc4357eec85e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='4004cced-7b24-4a7f-9383-454bb76c5fde'></a>

22/24