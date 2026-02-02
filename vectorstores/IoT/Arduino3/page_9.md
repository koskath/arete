<a id='e490e4c3-29ae-4e8b-aaf2-1983c458e4c4'></a>

12/4/25, 2:51 PM

<a id='27694a78-e806-4670-8d78-8403f7252240'></a>

ArduinoBLE | Arduino Documentation

<a id='259fde2c-d447-4065-983c-b6ccdc7cad85'></a>

ARDUINODOCS

<a id='b085d94b-e9d0-4507-b404-3330e198f9cf'></a>

## Returns
BLECharacteristic for provided parameters

## Example
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
17   Serial.println("Connecting ...");
18
19   if (peripheral.connect()) {
20     Serial.println("Connected");
21   } else {
22     Serial.println("Failed to connect!");
23     return;
24   }
25
26   // discover peripheral attributes
27   Serial.println("Discovering attributes...");
```

<a id='b08a0186-3bea-4c37-8a61-87c1a39ea511'></a>

Was this article helpful?
---
[Thumbs up icon] [Thumbs down icon]

<a id='9bee1561-bcee-4231-abfd-39b2c99b4ee5'></a>

## Connect and Contribute

---

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='872c7539-22dc-4c0f-b909-ec48d7193f86'></a>

© 2025 Arduino

Terms Of Service Privacy Policy Security Cookie Settings

<a id='617a3afd-ffc1-4b60-ad73-d3d01162ee8d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='d5fa02bd-29c3-4cec-9b45-a9d0fc37bcba'></a>

9/9