<a id='ac660c7d-6ab0-4ad6-aa7d-2c91855c654e'></a>

12/4/25, 2:51 PM

<a id='77bc74bf-4a5b-4db5-9bf5-333d0aaf38ce'></a>

ArduinoBLE | Arduino Documentation

<a id='4b59ebbb-c1f9-483f-ac4b-c257c62c81b0'></a>

ARDUINODOCS

<a id='72f46fa7-b681-4317-84d6-e1dca3aa0803'></a>

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Ene
4   while (1);
5 }
6
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
19   Serial.println("Connecting ...");
20
21   if (peripheral.connect()) {
22     Serial.println("Connected");
23   } else {
24     Serial.println("Failed to connect!");
25     return;
26   }
27 }
28 // discover peripheral attributes
```

<a id='4406ded6-cd14-4e12-a109-c2018c18ff2e'></a>

bleDevice.hasService()

Query if the Bluetooth® Low Energy device has a particular service.

<a id='c5c6ecf2-34ce-4a7b-8268-8486945b031d'></a>

## Syntax

```
1 bleDevice.hasService(uuid)
2 bleDevice.hasService(uuid, index)
```

<a id='2f448e5e-6ac3-4370-b7f6-725e5aad5d4d'></a>

# Parameters

**uuid**: uuid to check (as a **String**)
**index**: optional, index of service to check if the device provides
more than on. Defaults to 0, if not provided.

<a id='3fdb31a8-8338-49aa-aed4-e1c1966d3d32'></a>

## Returns

**true**, if the device provides the service,
**false** otherwise.

<a id='de35ced4-a6f8-48ce-8c47-1fbc84beac24'></a>

Example

[           ]

<a id='a18e5be9-2432-49a6-8c16-daa34b810678'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='95ef0cd5-b3b4-4b5c-9eb8-b4100a1d8a4d'></a>

14/24