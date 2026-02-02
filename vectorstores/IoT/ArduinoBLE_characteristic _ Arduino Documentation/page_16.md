<a id='b1f94f9f-164b-4f8d-85ec-adf578d4672c'></a>

12/4/25, 2:50 PM

<a id='a6f6afe4-ea6c-404e-a595-22ad819d70c8'></a>

ArduinoBLE | Arduino Documentation

<a id='6e297ece-2f88-4fd9-8339-c6be7a480df3'></a>

ARDUINODOCS

<a id='1be42e9c-0b54-490a-b2b8-8fde7dd0e75e'></a>



<a id='8d1ebbba-7e52-4eb5-8fb8-b3f7089a6fa7'></a>

if (characteristic.hasDescriptor("2901")) {
    Serial.println("characteristic has descriptor");
}

<a id='2dac57a2-f835-40f6-a750-d73e071e8072'></a>

⌵ bleCharacteristic.descriptor()
Get a BLEDescriptor that represents a characteristics Bluetooth® Low Energy descriptor.

<a id='43413fb2-54cf-47e9-9cd6-bc5ceaaf37b5'></a>

## Syntax

```
1 bleCharacteristic.descriptor(index)
2 bleCharacteristic.descriptor(uuid)
3 bleCharacteristic.descriptor(uuid, index)
```

<a id='1c3b8b60-9ee7-485b-b840-8af969870346'></a>

Parameters

index: index of descriptor

uuid: uuid (as a String)

<a id='1db22ed4-32fc-4c43-84a9-cbfd4a0c4f41'></a>

## Returns

BLEDescriptor that represents a characteristics Bluetooth® Low Energy descriptor

<a id='5381120c-b65f-4223-9382-57e951ee3806'></a>

Example
```
1 if (characteristic.hasDescriptor("2901")) {
2   Serial.println("characteristic has descriptior
3 }
```

<a id='74766711-14aa-4227-af8b-82dc3aa9b325'></a>

bleCharacteristic.canRead()
Query if a Bluetooth® Low Energy characteristic is readable.

## Syntax

```
1 bleCharacteristic.canRead()
```

<a id='3f7c3ece-2596-4768-8202-8fad13910833'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='c0477f86-28b0-4d0d-9b4b-12974fe59961'></a>

16/22