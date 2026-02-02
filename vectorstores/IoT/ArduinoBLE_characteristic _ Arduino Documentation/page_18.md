<a id='116c1818-e691-4c34-8c99-b6dae3a089f9'></a>

12/4/25, 2:50 PM

<a id='70cd7a66-31c7-4050-ae07-4a7b1be77bcf'></a>

ArduinoBLE | Arduino Documentation

<a id='038a30b3-08b7-45d0-8f57-14eff5d590af'></a>

ARDUINODOCS

<a id='ca24e147-fcb1-4f54-b62a-bebf999fa905'></a>



<a id='5f35b3ba-e98e-4278-adbe-df0195e95f3e'></a>

Query if a Bluetooth® Low Energy characteristic is writable.

### Syntax

```
1 bleCharacteristic.canWrite()
```

<a id='3a7a3b0a-51fe-41e2-8cdf-3e1459633fa8'></a>

## Parameters

None

<a id='57f1b3fb-e893-4af5-967f-078b2aa89f0e'></a>

## Returns

**true**, if characteristic is writable,
**false** otherwise

<a id='15a7a4ab-6fed-4bc2-ad70-25d8aef81990'></a>

## Example

```
1 if (characteristic.canWrite()) {
2    Serial.println("characteristic is writable");
3 }
```

<a id='60116221-423d-469e-a4bb-4e536d78bd13'></a>

v bleCharacteristic.canSubscribe()
Query if a Bluetooth® Low Energy characteristic is subscribable.

<a id='3fdd724b-a939-4885-b371-fc7cb8bcbb5d'></a>

## Syntax

```
1 bleCharacteristic.canSubscribe()
```

<a id='0c440346-f9ca-4af7-a876-b1b39d14c206'></a>

Parameters

None

<a id='487662d0-0873-416e-9eeb-32620403d6fe'></a>

## Returns

**true**, if characteristic is subscribable,
**false** otherwise

<a id='eba40556-040a-4a4e-8b73-6a7bde0d2800'></a>

Example

<a id='a2a91539-8890-477c-abe6-702e993e3042'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='a242979c-743a-41ad-9d5a-bab11b1d8738'></a>

18/22