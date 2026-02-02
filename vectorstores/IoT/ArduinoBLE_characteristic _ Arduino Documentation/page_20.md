<a id='57fdcf08-53ea-46b7-b018-19c15b4dfc33'></a>

12/4/25, 2:50 PM

<a id='8e1bde96-f998-4e40-8b15-440ce6525cc0'></a>

ArduinoBLE | Arduino Documentation

<a id='130fffea-b6b7-49c2-b19c-7d9cdafc1f46'></a>

ARDUINODOCS

<a id='3ed88632-12e6-49eb-b10c-3f216cb82567'></a>



<a id='ca52daf9-9b93-4f76-abcc-e8851940e8f6'></a>

Query if a Bluetooth Low Energy characteristic is unsubscribable.

## Syntax

```
1 bleCharacteristic.canUnsubscribe()
```

<a id='7b758869-156f-48ea-a37d-1db9498859c9'></a>

## Parameters

None

<a id='0e665ba9-b02c-4a6f-9cd8-c929e54e2bc7'></a>

Returns

true, if characteristic is unsubscribable,
false otherwise

<a id='5eeedd14-399d-4501-9e02-fc247252855d'></a>

# Example

```java
1 if (characteristic.canUnsubscribe()) {
2   Serial.println("characteristic is unsubscribat
3 }
```

<a id='f8197cc8-cad9-4e40-9f69-428f61950251'></a>

> bleCharacteristic.unsubscribe()
Unsubscribe to a Bluetooth® Low Energy characteristics
notifications or indications.

<a id='90a70fdd-6e49-427f-9a92-b71cd53ba06c'></a>

## Syntax

```
1 bleCharacteristic.unsubscribe()
```

<a id='d6ffa511-1bdf-4c2a-9756-00e446c4d0ed'></a>

**Parameters**

None

<a id='cf82434f-3842-4976-8f12-4e599fcc1f56'></a>

Returns

true, on success,
false on failure

<a id='bbbd53f5-c78d-4f1d-aede-18f6643d8ff4'></a>

Example

<a id='effb768d-bae5-4611-8621-7d248dc332cd'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='817912ce-1e9a-4dab-a1c0-a17c845f1a4f'></a>

20/22