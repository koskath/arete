<a id='bc22fb37-e4e9-4ec0-963b-9a458cfdddf8'></a>

12/4/25, 2:50 PM

<a id='9219a5b1-a12f-4eb5-a80a-46babc430e36'></a>

ArduinoBLE | Arduino Documentation

<a id='7b12955a-303f-4d76-b193-1c5733a859fd'></a>

ARDUINODOCS

<a id='93b363d4-6f8e-48a5-895a-8f0672b7d15d'></a>

None

**Returns**

**true**, if characteristic is readable,
**false** otherwise

<a id='f833bd7d-d880-4e42-9634-7fcccad6be01'></a>

## Example

```
1 if (characteristic.canRead("2901")) {
2   Serial.println("characteristic is readable");
3 }
```

<a id='1b96c9d9-8b03-4572-b581-f8c1094c32ed'></a>

read

Perform a read request for the characteristic.

<a id='c149a355-958e-4a76-b1cd-f673307f005f'></a>

## Syntax

```
1 bleCharacteristic.read()
```

<a id='0c7fa313-3d5d-4f95-9586-cc40bbcdc2bb'></a>

Parameters

None

<a id='213d979e-6021-46ab-b927-e4e9c774ec54'></a>

## Returns

**true**, if successful,

**false** on failure

<a id='bd9da21c-eb95-4510-a38c-9beabf8f8c7b'></a>

# Example

```
1 if (characteristic.read()) {
2   Serial.println("characteristic value read");
3 
4   // ...
5 } else {
6   Serial.println("error reading characteristic");
7 }
```

<a id='ab647dff-6378-461d-8e3b-05dc97ffd425'></a>

v bleCharacteristic.canWrite()

<a id='bf627398-61f1-436f-82e7-fa74b21907de'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='a96522d2-dc81-4352-887c-94cd77eee6c8'></a>

17/22