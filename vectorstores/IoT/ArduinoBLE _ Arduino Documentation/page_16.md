<a id='02229d94-5a83-4697-8c1b-a044ade242c1'></a>

12/4/25, 2:49 PM

<a id='4156d761-15c8-485f-9afb-8ae36d86aee0'></a>

ArduinoBLE | Arduino Documentation

<a id='dacd2ed9-7066-4d8c-84de-c19e360f092f'></a>

ARDUINODOCS

<a id='0a2d31c3-7acf-4861-a4d1-9dba8f521efd'></a>



<a id='668e26ee-2e6b-46bd-8c84-29c7b14e808a'></a>

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energ
4 
5   while (1);
6 }
7 
8 Serial.println("BLE Central scan");
9 
10 // start scanning for peripheral
11 BLE.scanForAddress("aa:bb:cc:ee:dd:ff");
12 
13 
14 BLEDevice peripheral = BLE.available();
15 
16 if (peripheral) {
17   // ...
18 }
```

<a id='dc93a7ed-54cf-43d1-8dca-859d5c2e4cf4'></a>

√ BLE.scanForUuid()
Start scanning for Bluetooth® Low Energy devices that are advertising with a particular (service) UUID.

<a id='61055130-044d-4d74-a8ae-8faba5eabab4'></a>

## Syntax

```
1 BLE.scanForUuid(uuid)
2 BLE.scanForUuid(uuid, withDuplicates)
```

<a id='dc4e83c6-fd62-444b-adf6-a06d0d66c3c9'></a>

## Parameters

**uuid**: (service) UUID (as a **String**) to filter for
**withDuplicates**: optional, defaults to **false**. If **true**, advertisements received more than once will not be filtered.

<a id='119f02d4-b113-445d-8366-bfb84362c2db'></a>

# Returns

1 on success,
0 on failure.

<a id='7d5a5a28-aa67-48fa-a027-66eb4fe5f43e'></a>

Example

---

<a id='74a361cf-afdf-4797-9fb7-83f6af128be7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='6b0e518a-c9c6-4a58-b8ac-cc5adbd9a12e'></a>

23/26