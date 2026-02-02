<a id='92db9a23-2281-4867-88e1-31f477ea9d43'></a>

12/4/25, 2:51 PM

<a id='1b52d41a-3e3a-4c7e-ad44-6812886f7d71'></a>

ArduinoBLE | Arduino Documentation

<a id='40420958-e43d-4fb5-8caf-59d7b73eeca6'></a>

ARDUINODOCS

<a id='74a57665-4b20-4c7b-a132-3ba4539fdd16'></a>

___

<a id='afa50122-bad4-44c9-aafe-a81bf92a11d2'></a>

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
19   if (peripheral.connect()) {
20     Serial.println("Connected");
21   } else {
22     Serial.println("Failed to connect!");
23     return;
24   }
25 }
26 
27 // discover peripheral attributes
28 Serial.println("Discovering attributes ...");
```

<a id='6890b603-25dc-413a-a82a-4179553fa675'></a>

✓ bleDevice.characteristicCount()
Query the number of characteristics discovered for the Bluetooth®
Low Energy device.

<a id='ba279de0-0be0-4608-8e5c-272c5df0cc96'></a>

## Syntax

```
1 bleDevice.characteristicCount()
```

<a id='19bdfc84-c047-4eef-9339-b8d3ca3b93fb'></a>

Parameters

None

<a id='eddd4412-17de-4fe9-929c-20b353db935d'></a>

## Returns

The **number of characteristics** discovered for the Bluetooth® Low Energy device.

<a id='60ef4a8c-3806-4249-a37d-ed85c97fe2a9'></a>

Example

---

<a id='68b23d92-e001-4c8a-be0c-00f6c7e0dfd6'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='7dca9566-c9c0-4a6e-9ccc-c627c162cd23'></a>

16/24