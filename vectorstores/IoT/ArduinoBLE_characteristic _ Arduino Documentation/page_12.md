<a id='fb0cb680-aafe-4473-9fc3-b6426e7b3b8e'></a>

12/4/25, 2:50 PM

<a id='95c0c251-fdb7-4c62-b8b7-3de5e0de4fd4'></a>

ArduinoBLE | Arduino Documentation

<a id='5d7dee4c-28b0-4c2e-b4fa-96d148a804d7'></a>

ARDUINODOCS

<a id='af2223b6-f1c2-46ea-a907-bd5c7baf6667'></a>

**Parameters**

None

**Returns**

1 on success,
0 on failure

<a id='0cac5827-a374-40a6-be23-7f511907b86d'></a>

Example

```
1 // create button characteristic and allow remote (
2 BLEByteCharacteristic buttonCharacteristic("19B100
3 
4 
5 
6 buttonCharacteristic.broadcast();
```

<a id='e3e5e884-f2a0-425a-9318-279776baac77'></a>

- bleCharacteristic.written()
  Query if the characteristic value has been written by another
  Bluetooth® Low Energy device.

<a id='6c974819-f85b-4a8f-9479-5fcd1ec0b73c'></a>

## Syntax

```
1 bleCharacteristic.written()
```

<a id='a4097ce8-b5a9-403d-b9b4-ac4606810a6a'></a>

Parameters

None

<a id='342fd312-6402-49ea-ab63-cb2099a02324'></a>

## Returns

**true** if the characteristic value has been written by another Bluetooth® Low Energy device,

**false** otherwise

<a id='1cf58b9f-bca4-4a40-a013-d6b63c6abf93'></a>

Example

___

<a id='db889de1-4e83-477d-8a13-ec3f42330dbe'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='4090c8ca-78c1-4a85-971f-f1f4a72f756e'></a>

12/22