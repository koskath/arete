<a id='32ffc04a-0c27-4d61-ac19-992a7b2f12b4'></a>

12/4/25, 2:51 PM

<a id='03a9d16c-444d-4646-9724-b7760f91cc37'></a>

ArduinoBLE | Arduino Documentation

<a id='4b32ba38-0848-45c7-8951-18a0c1d0dff9'></a>

ARDUINODOCS

<a id='38e77556-1c75-4d45-87d0-85b6a7a4e367'></a>

### Parameters
None

<a id='afdf15b8-b6e8-4248-b485-ab7bd44be437'></a>

### Returns

The **number of characteristics** discovered for the Bluetooth® Low Energy service.

<a id='7cab91bb-e05c-42e5-86a8-888c53ddabc7'></a>

Example

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy...");
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
14 if (peripheral) {
15   // ...
16
17   Serial.println("Connecting ...");
18
19   if (peripheral.connect()) {
20     Serial.println("Connected");
21   } else {
22     Serial.println("Failed to connect!");
23     return;
24   }
25 }
26
27 // discover peripheral attributes
28 Serial.println("Discovering attributes...");
```

<a id='5679e312-610f-488e-98ac-15afc87ec234'></a>

√ bleService.hasCharacteristic()
Query if the Bluetooth® Low Energy service has a particular
characteristic.

<a id='51986cbd-127d-4bfa-8261-e4a8d1a7abd2'></a>

## Syntax

```
bleservice.hasCharacteristic(uuid)
bleservice.hasCharacteristic(uuid, index)
```

<a id='bc93d281-28ed-4234-bde5-a8d885ce137e'></a>

Parameters

<a id='edacbd4b-4067-483a-b5be-0053551993ad'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='ee36547e-2d36-49a6-b22b-45ebc18f9e13'></a>

7/9