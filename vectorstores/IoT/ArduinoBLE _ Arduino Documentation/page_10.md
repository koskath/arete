<a id='0427e091-00d7-4f07-917c-238ec73389b9'></a>

12/4/25, 2:49 PM

<a id='d4d8ba53-461d-4b9a-9113-c03fe5f989e2'></a>

ArduinoBLE | Arduino Documentation

<a id='c43d06a3-7071-411d-a4c4-83b6b23ef87c'></a>

ARDUINODOCS

<a id='15d009a9-6945-441b-adf9-7054dbdaf4d5'></a>

BLE.setAdvertisedService()
Set the advertised service UUID used when advertising to the value
of the BLEService provided.

<a id='acdce79a-0ead-4528-83ab-b7351eef6c6b'></a>

## Syntax

```
1 BLE.setAdvertisedService(bleService)
```

<a id='80ba4f5a-c9b0-4906-bb7d-83cab42edf54'></a>

Parameters

bleService: BLEService to use UUID from

<a id='cbcefd3e-b3c7-43d3-b9e1-4f06374ae52c'></a>

Returns

Nothing

<a id='71ccfded-30c5-42d7-ba0d-e3c36911f875'></a>

Example

```
1 BLEService ledService("19B10000-E8F2-537E-4F6C-D1
2 
3 // ...
4 
5 // begin initialization
6 if (!BLE.begin()) {
7   Serial.println("starting Bluetooth® Low Energ
8 
9   while (1);
10 }
11 
12 BLE.setAdvertisedService(ledService);
13 
14 // ...
15 
16 // start advertising
17 BLE.advertise();
```

<a id='5088fb9b-6339-43cc-9351-6bdb7ac3ad50'></a>

### BLE.setManufacturerData()
Set the manufacturer data value used when advertising.

### Syntax

```
1 BLE.setManufacturerData(data, length)
```

<a id='5ada2a73-72b0-41da-a84f-a8e36074137f'></a>

Parameters

<a id='a36ba6c6-a014-415b-ac53-21bfe493a1d7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='487d480d-c7b5-4cdd-8bc8-beecb99bf9fa'></a>

11/26