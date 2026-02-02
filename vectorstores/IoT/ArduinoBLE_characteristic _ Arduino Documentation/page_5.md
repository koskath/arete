<a id='e92bed01-0530-4d76-9700-a3c5e17b3f06'></a>

12/4/25, 2:50 PM

<a id='e6c82615-3222-41ee-b88c-14c740ec5291'></a>

ArduinoBLE | Arduino Documentation

<a id='d3f216bc-2923-452a-a3cb-72d090f1dda0'></a>

ARDUINODOCS

<a id='569395a0-9861-408f-92f7-8b10fec6ac15'></a>

Used to enable the characteristics board offers in a service or interact with
characteristics a remote board provides.

<a id='3ce5a001-148c-4d24-9bf7-6cd2e422f519'></a>

BLECharacteristic()

Create a new Bluetooth® Low Energy characteristic.

## Syntax

```
BLECharacteristic(uuid, properties, valueSize)
BLECharacteristic(uuid, properties, valueSize, fixedLength)
BLECharacteristic(uuid, properties, stringValue)

BLEBoolCharacteristic(uuid, properties)
BLEBooleanCharacteristic(uuid, properties)
BLECharCharacteristic(uuid, properties)
BLEUnsignedCharCharacteristic(uuid, properties)
BLEByteCharacteristic(uuid, properties)
BLEShortCharacteristic(uuid, properties)
BLEUnsignedShortCharacteristic(uuid, properties)
BLEWordCharacteristic(uuid, properties)
BLEIntCharacteristic(uuid, properties)
BLEUnsignedIntCharacteristic(uuid, properties)
BLELongCharacteristic(uuid, properties)
BLEUnsignedLongCharacteristic(uuid, properties)
BLEFloatCharacteristic(uuid, properties)
BLEDoubleCharacteristic(uuid, properties)
```

<a id='bc32a0c8-9cfe-47bf-9aea-75ab427ee719'></a>

# Parameters
uuid: 16-bit or 128-bit UUID in **String** format
properties: mask of the properties (BLEBroadcast, BLERead,
BLEWriteWithoutResponse, BLEWrite, BLENotify, BLEIndicate)
valueSize: (maximum) size of characteristic value
fixedLength: if true, size of characteristic value is fixed
stringValue: value as a string

<a id='0ba8e4af-fcc6-48ce-b46d-bc2f9e46558f'></a>

## Returns

New **BLECharacteristic** with the specified **UUID** and value

<a id='776217be-ed82-48ae-aa4c-ba589e204ac8'></a>

Example

```
1 // Bluetooth® Low Energy Battery Level Characteristic
2 BLEUnsignedCharCharacteristic batteryLevelChar("2A19",
3 BLERead | BLENotify); // remote clients will be able to read and subscribe to notifications
```

<a id='f97e8e73-9171-4c04-a2a1-5bd6ded267ea'></a>

bleCharacteristic.uuid()

<a id='b16e4bb5-f17e-4454-9be5-7fa2060aaae7'></a>

Query the UUID of the specified BLECharacteristic

<a id='fb4aecdc-3732-4c9c-9261-c0085b7f7060'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='95b009d5-92a4-4a36-9c78-4488f96ee1d2'></a>

5/22