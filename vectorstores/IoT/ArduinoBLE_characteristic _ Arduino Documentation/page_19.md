<a id='ebf27ca2-1b14-4723-aa9a-90c606c47cc1'></a>

12/4/25, 2:50 PM

<a id='befab821-f810-4a14-ac20-f5085f374aa1'></a>

ArduinoBLE | Arduino Documentation

<a id='18c81feb-906c-4354-ac48-6bf29ed9ab6a'></a>

ARDUINODOCS

<a id='5b8c04e1-ab46-4de0-a111-7b7f117161d6'></a>



<a id='87e56706-a390-425d-8ede-b519838a1dbd'></a>

```
1 if (characteristic.canSubscribe()) {
2   Serial.println("characteristic is subscribable");
3 }
```

<a id='db89acf2-aed3-4f77-97e5-744106fc976b'></a>

> bleCharacteristic.subscribe()
> Subscribe to a Bluetooth® Low Energy characteristics notification or indications.

<a id='5edd635a-4921-431b-b5be-25f9dfce5b4f'></a>

**Syntax**

```
1 bleCharacteristic.subscribe()
```

<a id='81c4c12d-104f-4a56-b0da-a62310cc562f'></a>

## Parameters

None

<a id='f4a91d6c-0e81-4edb-a162-4d35ceb31820'></a>

**Returns**

**true**, on success,
**false** on failure

<a id='e43eb9a9-faad-462e-b59e-24c822d4e767'></a>

Example

```
1 // ...
2
3 // retrieve the simple key characteristic
4 BLECharacteristic simpleKeyCharacteristic = peripheral.getCharacteristic(SIMPLE_KEY_CHARACTERISTIC_UUID);
5
6 // subscribe to the simple key characteristic
7 Serial.println("Subscribing to simple key characteristic...");
8 if (!simpleKeyCharacteristic) {
9   Serial.println("no simple key characteristic found!");
10   peripheral.disconnect();
11   return;
12 } else if (!simpleKeyCharacteristic.canSubscribe()) {
13   Serial.println("simple key characteristic is not subscribable!");
14   peripheral.disconnect();
15   return;
16 } else if (!simpleKeyCharacteristic.subscribe()) {
17   Serial.println("subscription failed!");
18   peripheral.disconnect();
19   return;
20 }
21
22 // ...
```

<a id='726bece7-8c2a-4ae0-85f6-b3aca547cb50'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='2d40fec9-c444-4ab1-80f0-ea9da586fc36'></a>

19/22