<a id='110a2998-a832-4afd-b39e-ba4034753d2f'></a>

12/4/25, 2:50 PM

<a id='f14fb5cc-88bf-4340-bdfd-b93aeb0fc308'></a>

ArduinoBLE | Arduino Documentation

<a id='1a459f04-a0d0-46a6-988b-79da2cc9e4dd'></a>

ARDUINODOCS

<a id='c5b788c8-5436-4527-a980-f837f81cd095'></a>



<a id='afe30df5-5a00-496e-b379-15e9bdabcac3'></a>

## Syntax

```
1 bleCharacteristic.uuid()
```

<a id='b54a55f3-3cec-402d-b60c-974213bc8a5f'></a>

Parameters

None

<a id='f9f80d5b-1feb-4cf5-8813-8785fb052230'></a>

**Returns**

**UUID** of the Bluetooth® Low Energy service as a **String**.

<a id='0bd4fcc7-cc04-4ecb-a295-c69422a635ae'></a>

Example

```
1 // Bluetooth® Low Energy LED Switch Characteristic
2 BLEByteCharacteristic switchCharacteristic("19B100
3
4
5 Serial.print("Switch characteristic UUID = ");
6 Serial.println(switchCharacteristic.uuid());
```

<a id='ae5d2d7a-b1f6-414e-bb3e-0ec9e530e1b7'></a>

bleCharacteristic.properties()

Query the property mask of the specified BLECharacteristic.

<a id='0ed1e0f6-c8ba-450d-bbce-5318b18f232a'></a>

## Syntax

```
1 bleCharacteristic.properties()
```

<a id='928e0dfd-6644-4eec-9946-f9c1e7be1c22'></a>

Parameters

None

<a id='33293a11-06cf-4c5f-ae3d-dd92f1a8f648'></a>

## Returns

Properties of the characteristic masked (BLEBroadcast, BLERead, BLEWriteWithoutResponse, BLEWrite, BLENotify, BLEIndicate)

<a id='9d903df9-cdbe-43ca-9ca5-4fb5439cb8f4'></a>

## Example

[Empty input field]

<a id='2a3ab0e3-f349-4580-bc0e-e7f1fd2932fb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='14cd2798-e30b-4efb-88b0-1ae348bb0c9d'></a>

6/22